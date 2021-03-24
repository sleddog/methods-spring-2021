public class FizzBuzz {

    public static String FizzBuzz(int n) {
        String result = "";
        for (int i = 1; i <= n; i++) {
            result = "";
            if (i % 3 == 0)
                result += "Fizz";
            if (i % 5 == 0)
                result += "Buzz";
            if (i % 7 == 0)
                result += "Ping";
            if (i % 11 == 0)
                result += "Pong";

            if (result.length() == 0)
                result += Integer.toString(i);

            System.out.println(result);
        }
        return result;
    }
    public static void main(String[] args) {

        int n = Integer.parseInt(args[0]);
        FizzBuzz(n);
    }
}

