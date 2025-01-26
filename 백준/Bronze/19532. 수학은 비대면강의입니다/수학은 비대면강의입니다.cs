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
        int a = input[0];
        int b = input[1];
        int c = input[2];
        int d = input[3];
        int e = input[4];
        int f = input[5];

        for (int x = -999; x <= 999; x++)
        {
            for (int y = -999; y <= 999; y++)
            {
                if ((a * x + b * y == c) && (d * x + e * y == f))
                {
                    sb.Append($"{x} {y}");
                    Console.WriteLine(sb);
                    return; 
                }
            }
        }
    }
}
