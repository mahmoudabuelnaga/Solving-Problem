import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class JavaSubstringComparisons {

    public static void bubblesort(String[] arr) {
        for (int i=0; i < arr.length -1; i++){
            for (int j=0; j < arr.length - i - 1; j++){
                if (arr[j].compareTo(arr[j+1]) > 0) {
                    String temp = arr[j].toString();
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }

    public static String[] getSubstrings(String s, int k) {
        String[] substrings = new String[s.length() - k + 1];
        for (int i = 0; i < substrings.length; i++) {
            substrings[i] = s.substring(i, i + k);
        }
        bubblesort(substrings);
        return substrings;
    }

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        
        // Complete the function
        String[] arr = getSubstrings(s, k);
        // 'smallest' must be the lexicographically smallest substring of length 'k'
        smallest = arr[0];
        // 'largest' must be the lexicographically largest substring of length 'k'
        largest = arr[arr.length - 1];
        
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        // Scanner scan = new Scanner(System.in);
        // String s = scan.next();
        // int k = scan.nextInt();
        // scan.close();
      
        System.out.println(getSmallestAndLargest("welcometojava", 3));
    }
}
