using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        while (true)
        {
            int N = int.Parse(Console.ReadLine());
            if (N == 0) break;
            sb.AppendLine(fibonach(N).ToString());
        }
        Console.WriteLine(sb);
    }
    //fn(n) + fn(n-1)
    static int fibonach(int box) {
        int result = 1;
        int count = 1;
        int gap = 3;
        for (int i = 1; i < box; i++) {
            count += gap;
            gap += 2;
            result += count;
        }
        return result;
    }
}