using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{ 
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        sb.AppendLine(Math.Pow(int.Parse(Console.ReadLine()), 2).ToString());
        sb.AppendLine("2");
        Console.WriteLine(sb.ToString());
    }
}
