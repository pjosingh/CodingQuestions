package CrackingTheCodingInterviews.Arrays;

// pending 
public class OnePointThree {

    // remove duplicate characters from char arr without using additional space

    private static void removeDuplicates(char [] target) {
        

        int tail = 1; // this is the last index till we have unique numbers, from this number we have first duplicate

        for (int i=1; i<target.length; i++) {
            char current = target[i];

            int j;
            for (j=0 ; j < tail; j++) {
                if (current == target[j]) {
                    break; // this breaks when we find a duplicate, so while checking, we don't increment tail later. which means tail will point to first duplicate.
                }
            }
            if (j == tail) {
                target[tail] = target[i];
                tail ++;
            }
            
        }
        if (tail < target.length)
            target[tail] = 0;
    }
    public static void main(String ar[]) {
        runTestCase("abcda");
        runTestCase("abc");
        runTestCase("abac");
        runTestCase("abaccc"); // this use case doesn't work 
    }

    private static void runTestCase(String target) {
        char [] sample1 = target.toCharArray();
        removeDuplicates(sample1);
        System.out.println(sample1);
    }
    
}
