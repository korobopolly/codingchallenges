using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static int run = 0; // 함수 호출 카운트 (static으로 선언)

    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        int n = int.Parse(Console.ReadLine());
        int[] A = new int[n];
        int result = MenOfPassion(A, n);
        sb.AppendLine(run.ToString());
        sb.AppendLine(result.ToString());
        Console.WriteLine(sb.ToString());
    }

    static int MenOfPassion(int[] A, int n)
    {
        run ++;
        int i = n / 2; // ⌊n / 2⌋ 내림
        return A[i]; // 코드1
    }
}
