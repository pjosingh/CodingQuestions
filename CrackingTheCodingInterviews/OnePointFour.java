import java.util.Arrays;

public class OnePointFour {

    // check two strings are anagrams or not

    // solution 1
    private static boolean checkAnagram(String a, String b) {
        char [] aArray = a.toCharArray();
        char [] bArray = b.toCharArray();

        Arrays.sort(aArray);
        Arrays.sort(bArray);
        return new String(aArray).equals(new String(bArray));
    }

    public static void main(String ar[]) {
        System.out.println(checkAnagram("abc", "bca"));
        System.out.println(checkAnagram("abc", "bcaa"));
    }
    
}
