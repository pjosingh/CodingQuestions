package CrackingTheCodingInterviews.Arrays;

import java.util.zip.Checksum;

class OnePointOne {


    // string has all unique characters 

    private static boolean checkString(String target) {

        char check[] = new char[26];

        for (int i=0; i<target.length(); i++) {
            check[target.charAt(i)-'a']++;
            if (check[target.charAt(i)-'a'] > 1) {
                return false;
            }

        }

        return true;
    }


    public static void main(String ar[]) {
        System.out.println(checkString("aa"));
        System.out.println(checkString("abc"));
    }
}