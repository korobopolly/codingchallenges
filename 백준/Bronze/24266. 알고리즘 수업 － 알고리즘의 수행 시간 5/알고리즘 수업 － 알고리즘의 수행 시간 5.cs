using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        long N = long.Parse(Console.ReadLine());
        long pow = N * N * N;
        sb.AppendLine(pow.ToString());
        sb.AppendLine("3");
        Console.WriteLine(sb.ToString());
    }
}
