using System;
using System.IO;
using System.Text;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
            // 점의 개수 입력
            int N = int.Parse(Console.ReadLine());

            // (x, y) 쌍을 담을 배열 혹은 리스트
            // N이 최대 100,000이므로 배열로 잡아도 좋습니다.
            var points = new (int x, int y)[N];

            // 점 정보 입력 받기
            for (int i = 0; i < N; i++)
            {
                string[] line = Console.ReadLine().Split();
                int x = int.Parse(line[0]);
                int y = int.Parse(line[1]);
                points[i] = (x, y);
            }

            // 정렬: y 오름차순, y가 같으면 x 오름차순
            Array.Sort(points, (a, b) =>
            {
                if (a.y == b.y)
                    return a.x.CompareTo(b.x);
                return a.y.CompareTo(b.y);
            });

            // 빠른 출력을 위해 StringBuilder 사용
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < N; i++)
            {
                sb.Append(points[i].x).Append(' ')
                  .Append(points[i].y).Append('\n');
            }

            // 결과 한 번에 출력
            Console.Write(sb.ToString());
        }
}
