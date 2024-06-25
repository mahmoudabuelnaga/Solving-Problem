import java.util.*;

public class NumberFormat {

    public static void main(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        double payment = scanner.nextDouble();
//        scanner.close();

        Double payment = 12324.134;

        // Write your code here.
        String us = java.text.NumberFormat.getCurrencyInstance(Locale.US).format(payment);
        String india = java.text.NumberFormat.getCurrencyInstance(new Locale("en", "IN")).format(payment);
        String china = java.text.NumberFormat.getCurrencyInstance(Locale.CHINA).format(payment);
        String france = java.text.NumberFormat.getCurrencyInstance(Locale.FRANCE).format(payment);

        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}