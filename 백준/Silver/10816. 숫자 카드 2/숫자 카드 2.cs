using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        // StringBuilder를 사용하여 출력 성능 최적화
        StringBuilder sb = new StringBuilder();

        int N = int.Parse(Console.ReadLine());
        var countedCard = new Dictionary<string, int>();

        var line = Console.ReadLine().Split();
        for (int i = 0; i < N; i++)
        {
            string card = line[i];

            // 키가 존재하지 않는 경우 기본값 0을 할당
            if (!countedCard.ContainsKey(card))
            {
                countedCard[card] = 0;
            }

            countedCard[card] += 1;
        }

        int M = int.Parse(Console.ReadLine());
        var cmd = Console.ReadLine().Split();
        for (int j = 0; j < M; j++) {
            countedCard.TryGetValue(cmd[j], out int value);
            sb.Append($"{value} "); // 번호를 결과에 추가
        }

        // 최종 결과 출력
        Console.WriteLine(sb.ToString());
    }
}