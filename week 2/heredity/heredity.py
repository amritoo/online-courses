import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    # make a gene dict for (person, gene_num)
    gene = {}
    for person in people:
        if person in one_gene:
            gene[person] = 1
        elif person in two_genes:
            gene[person] = 2
        else:
            gene[person] = 0

    # calculate joint distribution
    p = 1.0
    for person, gene_num in gene.items():
        # probability of gene, given no parents
        prob_gene = PROBS["gene"][gene_num]

        # if has parents, calculate differently
        if has_parents(people[person]):
            f_get = get_prob(gene[people[person]["father"]])
            m_get = get_prob(gene[people[person]["mother"]])

            if gene_num == 0:    # got from neither parents
                prob_gene = (1 - f_get) * (1 - m_get)
            elif gene_num == 1:  # got from one parent
                prob_gene = f_get * (1 - m_get) + (1 - f_get) * m_get
            else:   # got from both parents
                prob_gene = f_get * m_get

        # probability of given trait
        if person in have_trait:
            p *= prob_gene * PROBS["trait"][gene_num][True]
        else:
            p *= prob_gene * PROBS["trait"][gene_num][False]

    return p


def get_prob(gene):
    """
    Returns probability of passing down gene, given number of gene
    """
    if gene == 2:
        return 1 - PROBS["mutation"]
    elif gene == 1:
        return 0.5
    else:
        return PROBS["mutation"]


def has_parents(person):
    """
    Returns true if person has parents listed in given dict
    """
    if person["mother"] and person["father"]:
        return True
    return False


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person, details in probabilities.items():
        # update gene
        if person in one_gene:
            details["gene"][1] += p
        elif person in two_genes:
            details["gene"][2] += p
        else:
            details["gene"][0] += p

        # update trait
        if person in have_trait:
            details["trait"][True] += p
        else:
            details["trait"][False] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities.values():
        # normalize gene
        total = sum(person["gene"].values())
        for gene in person["gene"]:
            person["gene"][gene] /= total

        # normalize trait
        total = sum(person["trait"].values())
        for trait in person["trait"]:
            person["trait"][trait] /= total


if __name__ == "__main__":
    main()
