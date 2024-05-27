package test;
import java.sql.SQLOutput;
import java.util.Random;
import java.util.Scanner;

public class Iwanttoplay {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("수를 입력하세요 ( 예 : 6 + 8 ) > ");
        String input = s.nextLine();

        String[] parts = input.split(" ");
        // Double
        Double a = Double.parseDouble(parts[0]);
        String b = parts[1];
        Double c = Double.parseDouble(parts[2]);
        // Integer
        /*
        Integer a = Integer.parseInt(parts[0]);
        String b = parts[1];
        Integer c = Integer.parseInt(parts[2]);
        */

        switch (b) {
            case "+":
                System.out.println("결과 : " + a + " + " + c + " = " + (a+c));
                break;
            case "-":
                System.out.println("결과 : " + a + " - " + c + " = " + (a-c));
                break;
            case "*":
                System.out.println("결과 : " + a + " * " + c + " = " + (a*c));
                break;
            case "/":
                System.out.println("결과 : " + a + " / " + c + " = " + (a/c));
                break;
/*            case "^":
                System.out.println(a + " ^ " + c + " = " + (a^c));
                break;
*/
        }
    }
}
