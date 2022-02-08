package leetcode;

class Largest {

    private static int getSecondLargest(int n[]) {

        // if size of array is 0, then this will throw exception
        int largest = n[0];
        
		int second = 0;
		
		for(int i = 1; i < n.length; i++) {
            if(largest < n[i] ) {
                second = largest;
                largest = n[i];
            }
            else {
                // this should be &&, not &. 
                // if(second< n[i] & n[i] < largest ) 
                //     second = n[i];
                if(second < n[i] && n[i] < largest ) 
                    second = n[i];
            }
		}
        return second;
    }
    public static void main(String ar[]) {
        int input1[] = {1,2,3,4,5};
        System.out.println(getSecondLargest(input1));
        int input2[] = {5,4,3,2,1};
        System.out.println(getSecondLargest(input2));

        int input3[] = {-1,-2,-3,-4,-5};
        //wrong output. Gives 0 as output. Because you initialized second with 0. It should be initilized with Integer.MIN_VALUE
        System.out.println(getSecondLargest(input3));
    }
}