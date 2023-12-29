package week1.homework2;

import java.util.Queue;
import java.util.Stack;

/*
 * SD2x Homework #2
 * Implement the method below according to the specification in the assignment description.
 * Please be sure not to change the method signature!
 */

public class HtmlValidator {
    /*
     * isValidHtml should take as input a Queue of HtmlTags and return a Stack of HtmlTags that verifies the
     * correctness of the tag structure, according to the specification described below.
     *
     * The method should be implemented as follows:
     * If the HTML file is well formatted, the method should return an empty Stack. For example:
     * 		<html><body><h1>heading</h1><p>paragraph</p></body></html>
     * In this case, the closing tags match the opening tags, so the HTML is valid. When you get to the end of the file/Queue, the Stack is empty.
     * If the HTML file is not well formatted, the method should return the Stack in its current state (i.e., with its
     * current values) at the time the code determined that the tags were not balanced.
     *
     * Here are some example cases to consider:
     *
     * Example #1: Tags closed in incorrect order
     *		<html><body><p><b>Sentence here</p></b></body></html>
     * In this case, you would push all opening tags onto the Stack so that it looks like this:
     *		<b>
     *		<p>
     *		<body>
     * and, upon encountering a closing tag in the Queue, you would want to check that Stack to see if the correct match is present.
     * The first closing tag you encounter is </p>; however, the last opening tag (at the top of the Stack) is . That’s bad.
     * As soon as you determine that the HTML file is not valid, return the Stack of opening tags without popping off the
     * mismatched opening tag. In this case, the expected output would be a Stack containing (going from bottom to top): <html><body><p><b>
     *
     * Example #2: Closing tag with no opening tag
     *		<html><body>Correct<br/><b>Sentence</b> here</div></body></html>
     * In this case, the first closing tag that you encounter (</b> New Roman',serif; color: #222222; background: white;">)
     * does match its opening tag, but the next one (</div>) does not, so the expected output would be a Stack containing (going from bottom to top):
     *		<html><body>
     * Note that the <br/> tag is self-closing and should not be placed on the Stack!
     *
     * Example #3: Opening tag never closed
     *		<html><body><b>This is some text
     * In this case, the method reaches the end of the file/Queue and there are still items on the Stack, since those opening
     * tags were never closed. The expected output would be a Stack containing (going from bottom to top):
     *		<html><body><b>
     *
     * Example #4 (the tricky part!): Closing tag with no opening tag, everything okay until then
     *		<html><body><p>Hello, world!</p></body></html></p>
     * This is similar to Example #2 except that now when you encounter the closing tag that has no opening tag, the
     * Stack is empty since everything before then is matched. However, returning an empty Stack means that the file is
     * well formatted! In this case, though, you need to return null to indicate that the file is not well formatted.
     * Think about how you can tell the difference between when to return null and when to return an empty Stack.
     */
    public static Stack<HtmlTag> isValidHtml(Queue<HtmlTag> tags) {
        Stack<HtmlTag> stack = null;
        while (!tags.isEmpty()) {
            HtmlTag tag = tags.remove();
            if (tag.isSelfClosing()) continue;
            if (tag.isOpenTag()) {
                if (stack == null)
                    stack = new Stack<>();
                stack.push(tag);
                continue;
            }
            if (stack != null && stack.empty()) {
//                System.out.println("returning null");
                return null;
            } else if (stack != null && tag.matches(stack.peek())) {
                stack.pop();
            } else
                break;
        }
        return stack;
    }

}

