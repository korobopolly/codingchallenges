import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = Integer.parseInt(br.readLine());
        int[] count = new int[10001]; // 입력 숫자가 10,000 이하임

        // 입력 숫자 카운트
        for (int i = 0; i < N; i++) {
            count[Integer.parseInt(br.readLine())]++;
        }

        // 결과 출력
        for (int i = 1; i <= 10000; i++) {
            while (count[i] > 0) {
                bw.write(i + "\n");
                count[i]--;
            }
        }

        br.close();
        bw.flush();
        bw.close();
    }
}
