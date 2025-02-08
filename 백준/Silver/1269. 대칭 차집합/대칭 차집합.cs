using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        // 첫 번째 줄 입력 (필요한 경우 사용)
        var input = Console.ReadLine().Split().Select(int.Parse).ToArray();

        // 두 번째 줄 입력을 HashSet으로 바로 변환
        var set1 = new HashSet<string>(Console.ReadLine().Split());

        // 세 번째 줄 입력을 HashSet으로 바로 변환
        var set2 = new HashSet<string>(Console.ReadLine().Split());

        int result = 0;

        // line2의 요소 중 set1에 없는 것 카운트
        foreach (var line in set2)
        {
            if (!set1.Contains(line)) { result += 1; }
        }

        // line1의 요소 중 set2에 없는 것 카운트
        foreach (var line in set1)
        {
            if (!set2.Contains(line)) { result += 1; }
        }

        // 최종 결과 출력
        Console.WriteLine(result);
    }
}