import java.util.Arrays;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class BinarySearch {
    public static void main(String[] args) {
        int[] whitelist = Arrays.stream(args[0].split(",")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(whitelist);
        int key = Integer.parseInt(args[1]);
        int index = indexOf(whitelist, key);
        if (index != -1) {
            System.out.println("found key " + key + " at index " + index + " in " + Arrays.toString(whitelist));
        } else {
            System.out.println("key " + key + " not found in " + Arrays.toString(whitelist));
        }
    }

    public static int indexOf(int[] a, int key) {
        int lo = 0;
        int hi = a.length - 1;
        while (lo <= hi) {
            // Key is in a[lo..hi] or not present.
            int mid = lo + (hi - lo) / 2;
            if      (key < a[mid]) hi = mid - 1;
            else if (key > a[mid]) lo = mid + 1;
            else return mid;
        }
        return -1;
    }
}
