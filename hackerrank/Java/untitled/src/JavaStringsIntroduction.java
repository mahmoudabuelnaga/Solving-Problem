public class JavaStringsIntroduction {
    public static void main(String[] args) {
        String a = "java";
        String b = "java";

        int len = a.length() + b.length();

        int compare = a.compareTo(b);


        String concat = CapilizeFirstLetter(a) + " " + CapilizeFirstLetter(b);
        System.out.println(len);

        if (compare <= 0){
            System.out.println("No");
        } else{
            System.out.println("Yes");
        }

        System.out.println(concat);
    }

    public static String CapilizeFirstLetter(String str){
        return str.substring(0, 1).toUpperCase() + str.substring(1);
    }
}
