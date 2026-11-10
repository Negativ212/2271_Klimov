public class Main {
    public static void main(String[] args) {
        int[][] a = {
            {5, 3, 8},
            {2, 7, 0},
            {4, 0, 9}
        };
        boolean f = false;
        int row = -1, col = -1;

        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                if (a[i][j] == 0) {
                    f = true;
                    row = i;
                    col = j;
                    break;
                }
            }
            if (f) {
                break;         
            }
        }

        if (f) System.out.println("Первый ноль: " + row + " " + col);
        else System.out.println("Нулей нет");
    }
}