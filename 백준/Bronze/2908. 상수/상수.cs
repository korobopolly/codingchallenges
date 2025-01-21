using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        var input = Console.ReadLine().Split();
        for (int i = 0; i < 2; i++)
        {
            char[] charArray = input[i].ToCharArray();
            (charArray[0], charArray[2]) = (charArray[2], charArray[0]);
            input[i] = new string(charArray);
        }
        sb.Append(int.Parse(input[0]) > int.Parse(input[1]) ? int.Parse(input[0]) : int.Parse(input[1]));
        Console.WriteLine(sb.ToString());
    }
}
