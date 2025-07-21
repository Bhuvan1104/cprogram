// ReverseNumber.java
public class Revnum {
    public static void main(String[] args) {
        int number = 12345;
        int reverse = 0;

        System.out.println("Original number: " + number);

        while (number != 0) {
            int digit = number % 10;
            reverse = reverse * 10 + digit;
            number /= 10;
        }

        System.out.println("Reversed number: " + reverse);
    }
}
