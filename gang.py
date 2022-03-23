# 일단자바
'''
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;
 
public class Main {
        // N개의 화분, 각 K씩 ,연속된 A개의 화분에 B 만큼 물을 준다.
        // 1. A개의 화분에 B만큼 물을줌.
        // 2. 1씩감소
        // 3. 수분이 0이 된 화분은 죽는다.
        // 6 3 2 2
        // 3 3 3 3 3 3

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int []arr = new int[N];
        int res = 0;
        for(int i=0; i<arr.length; i++){
            arr[i] = K;
        }
        while(arr[0] != 0){            
            for(int i=0;i<A;i++){
                arr[i] += B;
            }
            for(int i=0; i<arr.length; i++){
                arr[i]--;
            }
            Arrays.sort(arr);
            res++;
        }
        System.out.println(res);
	}
}
'''
