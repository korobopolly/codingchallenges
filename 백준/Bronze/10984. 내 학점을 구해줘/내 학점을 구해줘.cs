using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;

class Program2
{
    static void Main(string[] args)
    {
        // 첫 번째 줄 입력 (필요한 경우 사용)
        var T = int.Parse(Console.ReadLine());
        for (int i = 0; i < T; i++)
        {
            float result = 0;
            float grade = 0;
            var N = int.Parse(Console.ReadLine());
            for (int j = 0; j < N; j++)
            {
                var line = Console.ReadLine().Split().Select(float.Parse).ToArray();
                grade += line[0];
                result += line[0] * line[1];
            }
            Console.WriteLine($"{grade} {result / grade}");
        }
    }
}