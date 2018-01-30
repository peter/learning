public class Gcd {
    // GCD - greatest common divisor of two integers a and b.
    // An intuitive and visual way to understand the problem is to think of it as
    // fitting square tiles in a rectangle with horizontal longer side a and vertical shorter side b.
    // The algorithm is based on realizing that if the tile is to fit in a and b it must also fit in a - b.
    // You thus take a - b (the remainder) or a % b (yields the same result but in fewer steps). You then
    // have a remainder that will be the new shorter side b and use the old b as the longer side a (you swap)
    // and recur.
    public static void main(String[] args) {
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        int gcd = gcd_recur(a, b);
        assert gcd == gcd_iter(a, b);
        System.out.println(String.format("gcd=%s: %s/%s -> %s/%s", gcd, a, b, a/gcd, b/gcd));
    }

    private static int gcd_recur(int a, int b) {
        if (b == 0) return a;
        return gcd_recur(b, a % b);
    }

    private static int gcd_iter(int a, int b) {
        while (b > 0) {
            int oldA = a;
            a = b;
            b = oldA % b;
        }
        return a;
    }
}
