using System;
using System.Linq;
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        int N = int.Parse(Console.ReadLine());
        for (int i = 0; i < N; i++) {
            sb.Append(new string('*', i+1));
            sb.AppendLine();
        }
        Console.WriteLine(sb.ToString());
    }
}
