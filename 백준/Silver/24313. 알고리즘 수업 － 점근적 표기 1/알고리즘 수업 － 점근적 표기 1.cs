using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{ 
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int a1 = input[0];
        int a0 = input[1];
        int c = int.Parse(Console.ReadLine());
        int n0 = int.Parse(Console.ReadLine());
        bool is_valid = false;
        for (int n = n0; n <= 100; n++)
        {
            if (a1 * n + a0 <= c * n) is_valid = true;
            else
            {
                is_valid = false;
                break;
            }
        }
        sb.AppendLine(is_valid ? "1" : "0");
        Console.WriteLine(sb.ToString());
    }
}
