using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        var result = new List<int>();
        int i = 666;
        while (result.Count < N) {
            if (is666(i.ToString())) result.Add(i);
            i++;
        }
        Console.WriteLine(result[^1]); // 최소값 출력
    }

    static bool is666 (string number)
    {
        for (int i = 0; i < number.Length - 2; i++) {
            if (number[i] == '6' && number[i + 1] == '6' && number[i + 2] == '6') return true; 
        }
        return false;
    }
}
