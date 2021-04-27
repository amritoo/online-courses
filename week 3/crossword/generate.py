import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for var, words in self.domains.items():
            remove = set()
            for word in words:
                if var.length != len(word):
                    remove.add(word)

            for word in remove:
                self.domains[var].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        overlap = self.crossword.overlaps[x, y]
        # If no overlap, then they are already consistant
        if overlap is None:
            return False

        remove = set()
        for x_word in self.domains[x]:
            no_value = True
            for y_word in self.domains[y]:
                # If for x_word there's a consistant y_word, check for next x_word
                if self.is_consistant(x_word, y_word, overlap):
                    no_value = False
                    break

            if no_value:
                remove.add(x_word)

        if len(remove) == 0:
            return False

        # Remove words
        for x_word in remove:
            self.domains[x].remove(x_word)
        return True

    def is_consistant(self, word1, word2, overlap):
        """
        Return true if word1 and word2 is consistant with overlap.
        """
        i, j = overlap
        if word1[i] == word2[j]:
            return True
        return False

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if arcs is None:
            # All arcs
            arcs = list(
                var for var, val in self.crossword.overlaps.items() if val
            )

        while len(arcs) > 0:
            x, y = arcs.pop(0)
            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False

                # Add additional arcs for maintaining arc consistency
                neighbors = self.crossword.neighbors(x)
                neighbors.discard(y)
                for z in neighbors:
                    arcs.append((z, x))
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        if len(self.crossword.variables) == len(assignment.keys()):
            return True
        return False

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # check if all values are distinct
        values = set(assignment.values())
        if len(assignment) != len(values):
            return False

        # check if all values are of correct length
        for var, val in assignment.items():
            if var.length != len(val):
                return False

        # check conflict between neighbors
        for x in assignment:
            for y in assignment:
                if x == y:
                    continue

                overlap = self.crossword.overlaps[x, y]
                if overlap and not self.is_consistant(assignment[x], assignment[y], overlap):
                    return False
        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # valid values for var, removing duplicate
        values = self.domains[var].difference(assignment.values())

        # unassigned neighbors
        neighbors = self.crossword.neighbors(var).difference(assignment.keys())

        # create result dict
        result = {}
        for val in values:
            count = 0
            # count number of not consistant values
            for neighbor in neighbors:
                overlap = self.crossword.overlaps[var, neighbor]
                for neighbor_val in self.domains[neighbor]:
                    if not self.is_consistant(val, neighbor_val, overlap):
                        count += 1
            result[val] = count

        result = [
            x[0]
            for x in sorted(result.items(), key=lambda item: item[1])
        ]
        return result

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        variables = self.crossword.variables.difference(assignment.keys())

        # create minimum remaining values set
        rem_value = 1000000000
        values = set()
        for var in variables:
            l = len(self.domains[var])
            if rem_value > l:
                rem_value = l
                values.clear()
                values.add(var)
            elif rem_value == l:
                values.add(var)

        # if only one value in set, then retrun
        if len(values) == 1:
            return values.pop()

        # create highest degree set
        degree = 0
        variables = set()
        for var in values:
            d = len(self.crossword.neighbors(var))
            if degree < d:
                degree = d
                variables.clear()
                variables.add(var)
            elif degree == d:
                variables.add(var)

        return variables.pop()

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment

        var = self.select_unassigned_variable(assignment)
        for val in self.order_domain_values(var, assignment):
            assignment[var] = val
            if self.consistent(assignment):
                result = self.backtrack(assignment)
                if result:
                    return result

            assignment.pop(var)

        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
