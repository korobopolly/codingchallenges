using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        //nC3 (i,j,k)
        long N = int.Parse(Console.ReadLine());
        sb.AppendLine((N * (N - 1) * (N - 2) / (3 * 2 * 1)).ToString());
        sb.AppendLine("3");
        Console.WriteLine(sb.ToString());
    }
}
