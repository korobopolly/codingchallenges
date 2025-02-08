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
        var N = int.Parse(Console.ReadLine());
        var list = new List<char>(new[] { 'U', 'O', 'S' });

        // 최종 결과 출력
        Console.WriteLine(list[(N-1) % 3]);
    }
}