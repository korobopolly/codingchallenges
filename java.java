//코딩테스트 문제 LV0

//주어진 코드는 변수에 데이터를 저장하고 출력하는 코드입니다. 아래와 같이 출력되도록 빈칸을 채워 코드를 완성해 주세요.

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        String message = "Let's go!";

        System.out.println("3\n2\n1");
        System.out.println(message);
    }
}

//일반적으로 두 선분이 이루는 각도는 한 바퀴를 360도로 하여 표현합니다. 따라서 각도에 360의 배수를 더하거나 빼더라도 같은 각을 의미합니다. 예를 들면, 30도와 390도는 같은 각도입니다.
//주어진 코드는 각도를 나타내는 두 정수 angle1과 angle2가 주어질 때, 이 두 각의 합을 0도 이상 360도 미만으로 출력하는 코드입니다. 코드가 올바르게 작동하도록 한 줄을 수정해 주세요.

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int angle1 = sc.nextInt();
        int angle2 = sc.nextInt();

        int sum_angle = angle1 + angle2;
        System.out.println(sum_angle%360);
    }
}

//2자리 이상의 정수 number가 주어집니다. 주어진 코드는 이 수를 2자리씩 자른 뒤, 자른 수를 모두 더해서 그 합을 출력하는 코드입니다. 코드가 올바르게 작동하도록 한 줄을 수정해 주세요.

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        int answer = 0;
        
        for(int i=0; number!=0; i++){
            answer += number % 100;
            number /= 100;
        }

        System.out.println(answer);
    }
}

// 퓨쳐종합병원에서는 접수한 환자가 진료받을 병과에 따라 자동으로 환자 코드를 부여해 주는 프로그램이 있습니다. 환자 코드의 마지막 네 글자를 보면 환자가 어디 병과에서 진료를 받아야 할지 알 수 있습니다. 예를 들어 환자의 코드가 "_eye"로 끝난다면 안과를, "head"로 끝난다면 신경외과 진료를 보게 됩니다. 환자 코드의 마지막 글자에 따른 병과 분류 기준은 다음과 같습니다.
// 마지막 글자	병과
// "_eye"	"Ophthalmologyc"
// "head"	"Neurosurgery"
// "infl"	"Orthopedics"
// "skin"	"Dermatology"
// 환자의 코드를 나타내는 문자열 code를 입력받아 위 표에 맞는 병과를 출력하도록 빈칸을 채워 코드를 완성해 주세요. 위 표의 단어로 끝나지 않는다면 "direct recommendation"를 출력합니다.

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String code = sc.next();
        String lastFourWords = code.substring(code.length()-4, code.length());

        if(lastFourWords.equals("_eye")){
            System.out.println("Ophthalmologyc");
        }
        else if(lastFourWords.equals("head")){
            System.out.println("Neurosurgery");
        }
        else if(lastFourWords.equals("infl")){
            System.out.println("Orthopedics");
        }
        else if(lastFourWords.equals("skin"))
        {
            System.out.println("Dermatology");
        }
        else
        {
            System.out.println("direct recommendation");
        }
    }
}

// 심폐소생술은 다음과 같은 순서를 통해 실시합니다.
// 심정지 및 무호흡 확인 [check]
// 도움 및 119 신고 요청 [call]
// 가슴압박 30회 시행 [pressure]
// 인공호흡 2회 시행 [respiration]
// 가슴압박, 인공호흡 반복 [repeat]
// 주어진 solution 함수는 심폐소생술을 하는 방법의 순서가 담긴 문자열들이 무작위 순서로 담긴 리스트 cpr이 주어질 때 각각의 방법이 몇 번째 단계인지 순서대로 담아 return하는 함수입니다. solution 함수가 올바르게 작동하도록 빈칸을 채워 solution 함수를 완성해 주세요.

// 제한사항
// cpr은 다음 문자열들이 한 번씩 포함되어 있습니다.
// "check", "call", "pressure", "respiration", "repeat"

class Solution {
    public int[] solution(String[] cpr) {
        int[] answer = {0, 0, 0, 0, 0};
        String[] basic_order = {"check", "call", "pressure", "respiration", "repeat"};

        for(int i=0; i<cpr.length; i++){
            for(int j=0; j<basic_order.length; j++){
                if(cpr[i].equals(basic_order[j])){
                    answer[i] = j+1;
                    break;
                }
            }
        }
        return answer;
    }
}

// ㅇㅇ시에서는 저수지가 하나 있는데, 도시 내에서 사용하는 모든 물은 이 저수지에 저장된 물을 끌어와 사용합니다. 이상 기후로 인해 극심한 가뭄이 예고된 상황에서, 지난 달의 물 사용량과 이번달부터 일정 기간 동안의 월별 물 사용량의 변화를 예측한 값을 이용해 몇 달 뒤 물이 부족해지는지 예측하려고 합니다.
// 이번달부터의 월별 물 사용량 변화를 예측한 값은 다음과 같이 리스트에 담겨 주어집니다.
// [10, -10, 10, -10, 10, -10, 10, -10, 10, -10]
// 리스트의 각 원소는 해당 월의 물 사용량이 전 달에 비해 몇 % 만큼 증가 또는 감소하는지를 나타냅니다.
// 예를 들어, 이번달의 물 사용량 (리스트의 첫 번째 원소)은 지난 달 보다 10% 증가한 값이며, 다음 달(리스트의 두 번째 원소)의 물 사용량은 이번달 사용량에서 10%만큼 감소한 값입니다.
// 자세한 값은 입출력 예시를 참고해 주세요.
// 현재 저수지에 저장된 물의 양을 나타내는 정수 storage와 지난 달 물 사용량을 나타내는 정수 usage, 월별 물 사용량이 전 달 대비 어떻게 변하는지 저장된 정수 리스트 change가 주어질 때 몇 달 뒤 물이 부족해지는지 return 하도록 solution 함수를 작성하려 합니다. 코드가 올바르게 작동하도록 한 줄을 수정해 solution 함수를 완성해 주세요. 가뭄이 끝날때 까지 저수지의 물이 남아 있다면 -1을 return합니다.

// 제한사항
// 1,000 ≤ storage ≤ 1,000,000
// 500 ≤ usage ≤ 30,000
// 1 ≤ change의 길이 ≤ 30
// -99 ≤ change[i] ≤ 500
// change[i] 가 양수일 경우 물 사용량은 전 달 보다 change[i]% 만큼 증가합니다.
// change[i] 가 음수일 경우 물 사용량은 전 달 보다 change[i]% 만큼 감소합니다.
// change[i] 가 0일 경우 물 사용량은 전 달과 동일합니다.
// 매달 물 사용량은 소수점 이하를 버린 정수로 계산합니다.
// 입출력 예
// storage	usage	change	result
// 5141	500	[10, -10, 10, -10, 10, -10, 10, -10, 10, -10]	-1
// 1000	2000	[-10, 25, -33]	1

class Solution {
    public int solution(int storage, int usage, int[] change) {
        int total_usage = 0;
        for(int i=0; i<change.length; i++){
            usage += usage * change[i] / 100;
            total_usage += usage;
            if(total_usage > storage){
                return i;
            }
        }
        return -1;
    }
}

// 영진이는 약속장소에 가기 위해 버스를 타려고 합니다. 버스에는 좌석이 총 seat개만큼 있습니다. 영진이는 버스 좌석에 앉아서 갈 수 있을지 궁금해합니다. 기점에서 출발한 버스가 영진이가 기다리는 정거장에 도착하기 전에 방문하는 각 정거장에서 승/하차한 승객 정보가 주어질 때, 영진이가 버스에 탄 순간 빈 좌석은 몇 개인지 구해주세요. 영진이가 기다리는 정거장에서는 영진이가 제일 먼저 버스에 탑승하며, 이전 정거장에서 버스에 탑승한 승객들은 남는 좌석이 있다면 항상 앉는다고 가정합니다. 또, 기점에서 출발하는 버스에는 승객이 0명 타고 있습니다.
// 예를 들어 다음은 좌석이 5개인 버스에 각 정거장에서 승/하차한 승객 정보를 나타냅니다. 영진이는 4번 정거장에서 기다리고 있으며, "On"은 승차한 승객, "Off"는 하차한 승객을 의미합니다.
// - 1번 정거장 : ["On", "On", "On"] (3명 승차, 0명 하차)
// - 2번 정거장 : ["Off", "On", "-"] (1명 승차, 1명 하차)
// - 3번 정거장 : ["Off", "-", "-"]  (0명 승차, 1명 하차)
// 위와 같은 경우, 1번 정거장에서 3명이 승차하고, 2번 정거장에서 1명 승차 1명 하차, 3번 정거장에서 1명이 하차했으므로 4번 정거장에 도착한 버스에는 2명이 타고 있습니다. 4번 정거장에서는 영진이가 가장 먼저 탑승하므로, 남아있는 좌석 수는 3개입니다.
// 주어진 solution함수는 버스의 좌석 개수 seat, 기점에서 출발한 버스가 순서대로 방문한 정거장에서 승객이 승/하차한 정보를 담은 2차원 문자열 리스트 passengers가 주어질 때, 버스에 남아있는 좌석의 개수를 return 하는 함수입니다. solution 함수가 올바르게 작동하도록 빈칸을 채워 solution함수를 완성해 주세요.

class Solution {
    public int solution(int seat, String[][] passengers) {
        int num_passenger = 0;
        for(int i=0; i<passengers.length; i++){
            num_passenger += func4(passengers[i]);
            num_passenger -= func3(passengers[i]);
        }
        int answer = func1(seat - num_passenger);
        return answer;
    }

    public int func1(int num){
        if(0 > num){
            return 0;
        }
        else{
            return num;
        }
    }
    public int func2(int num){
        if(num > 0){
            return 0;
        }
        else{
            return num;
        }
    }

    public int func3(String[] station){
        int num = 0;
        for(int i=0; i<station.length; i++){
            if(station[i].equals("Off")){
                num += 1;
            }
        }
        return num;
    }

    public int func4(String[] station){
        int num = 0;
        for(int i=0; i<station.length; i++){
            if(station[i].equals("On")){
                num += 1;
            }
        }
        return num;
    }
}

// 온라인 서비스를 이용하기 위해서 닉네임이 필요합니다. 이때 닉네임이 될 수 있는 조건은 다음과 같습니다.
// 닉네임의 길이가 4자 이상 8자 이하여야합니다.
// 닉네임에는 소문자 l과w, 대문자 O와 W를 사용할 수 없습니다.
// 이외의 영어 대소문자와 숫자는 모두 사용이 가능합니다.
// 주어진 solution 함수는 사용할 수 없는 닉네임 nickname을 받아 사용할 수 있는 닉네임으로 바꿔주는 함수입니다. 이때 닉네임을 변경하는 규칙은 다음과 같으며 첫 번째 규칙부터 순서대로 적용합니다.
// 소문자 l을 대문자 I로 변경합니다.
// 소문자 w를 두 개의 소문자 v, 즉 vv로 변경합니다.
// 대문자 W를 두 개의 대문자 V, 즉 VV로 변경합니다.
// 대문자 O를 숫자 0으로 변경합니다.
// 수정된 닉네임의 길이가 4 미만일 경우 뒤에 소문자 o를 길이가 4가 될때까지 이어붙입니다.
// 수정된 닉네임의 길이가 8보다 클 경우 8번째 문자까지만 사용합니다.
// 주어진 solution 함수에는 위의 규칙 중 올바르게 적용되지 않는 것이 있습니다. solution 함수가 올바르게 작동하도록 한 줄을 수정해주세요.

class Solution {
    public String solution(String nickname) {
        String answer = "";
        for(int i=0; i<nickname.length(); i++){
            if(nickname.charAt(i) == 'l'){
                answer += "I";
            }
            else if(nickname.charAt(i) == 'w'){
                answer += "vv";
            }
            else if(nickname.charAt(i) == 'W'){
                answer += "VV";
            }
            else if(nickname.charAt(i) == 'O'){
                answer += "0";
            }
            else{
                answer += nickname.charAt(i);
            }
        }
        while(answer.length() < 4){
            answer += "o";
        }
        if(answer.length() > 8){
            answer = answer.substring(0, 8);
        }
        return answer;
    }
}

// 주어진 초기 코드는 변수에 데이터를 저장하고 출력하는 코드입니다. 아래와 같이 출력되도록 빈칸을 채워 코드를 완성해 주세요.
// 출력 예시
// Spring is beginning
// 13
// 310

#include <iostream>

using namespace std;

int main(void) {
    string msg = "Spring is beginning";
    int val1 = 3;
    string val2 = "3";

    cout << msg << endl;
    cout << val1 + 10 << endl;
    cout << val2 + "10" << endl;

    return 0;
}

// 직각삼각형이 주어졌을 때 빗변의 제곱은 다른 두 변을 각각 제곱한 것의 합과 같습니다.
// 피타고라스.jpg
// 직각삼각형의 한 변의 길이를 나타내는 정수 a와 빗변의 길이를 나타내는 정수 c가 주어질 때, 다른 한 변의 길이의 제곱, b_square 을 출력하도록 한 줄을 수정해 코드를 완성해 주세요.

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int c = sc.nextInt();

        int b_square = (int)Math.pow(c,2) - (int)Math.pow(a,2);

        System.out.println(b_square);
    }
}

// 나이를 세는 방법은 여러 가지가 있습니다. 그중 한국식 나이는 태어난 순간 1살이 되며 해가 바뀔 때마다 1살씩 더 먹게 됩니다. 연 나이는 태어난 순간 0살이며 해가 바뀔 때마다 1살씩 더 먹게 됩니다. 각각 나이의 계산법은 다음과 같습니다.
// 한국식 나이 : 현재 연도 - 출생 연도 + 1
// 연 나이 : 현재 연도 - 출생 연도
// 출생 연도를 나타내는 정수 year와 구하려는 나이의 종류를 나타내는 문자열 age_type이 주어질 때 2030년에 몇 살인지 출력하도록 빈칸을 채워 코드를 완성해 주세요. age_type이 "Korea"라면 한국식 나이를, "Year"라면 연 나이를 출력합니다.

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();
        String age_type = sc.next();
        int answer = 0;

        if (age_type.equals("Korea")) {
            answer = 2030 - year + 1;
        }
        else if (age_type.equals("Year")) {
            answer = 2030 - year;
        }

        System.out.println(answer);
    }
}

// 진우는 돈을 모으기 위해 저축을 하려고 합니다. 목표로 하는 금액은 100만 원이며, 첫 달에 일정 금액을 넣은 뒤 70만 원까지는 매월 조금씩 저축하다가 70만 원 이후부터는 월 저축량을 늘려 빠르게 목표 금액을 달성하고자 합니다.
// 첫 달에 저축하는 금액을 나타내는 정수 start, 두 번째 달 부터 70만 원 이상 모일 때까지 매월 저축하는 금액을 나타내는 정수 before, 100만 원 이상 모일 때 까지 매월 저축하는 금액을 나타내는 정수 after가 주어질 때, 100만 원 이상을 모을 때까지 걸리는 개월 수를 출력하도록 빈칸을 채워 코드를 완성해 주세요.

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int start = sc.nextInt();
        int before = sc.nextInt();
        int after = sc.nextInt();

        int money = start;
        int month = 1;
        while (money < 70) {
            money += before;
            month++;
        }
        while (money  < 100) {
            money += after;
            month++;
        }

        System.out.println(month);
    }
}

// 여름이는 강아지를 산책시키려고 합니다. 여름이는 2차원 좌표평면에서 동/서/남/북 방향으로 1m 단위로 이동하면서 강아지를 산책시킵니다. 산책루트가 담긴 문자열 route가 주어질 때, 도착점의 위치를 return하도록 빈칸을 채워 solution함수를 완성해 주세요.
// route는 "N", "S", "E", "W"로 이루어져 있습니다.
// "N"은 북쪽으로 1만큼 움직입니다.
// "S"는 남쪽으로 1만큼 움직입니다.
// 북쪽으로 -1만큼 움직인 것과 같습니다.
// "E"는 동쪽으로 1만큼 움직입니다.
// "W"는 서쪽으로 1만큼 움직입니다.
// 동쪽으로 -1만큼 움직인 것과 같습니다.
// 출발점으로부터 [동쪽으로 떨어진 거리, 북쪽으로 떨어진 거리]형태로 강아지의 최종 위치를 구해서 return해야 합니다.
// 출발점을 기준으로 서쪽, 남쪽에 있는 경우는 동쪽, 북쪽으로 음수만큼 떨어진 것으로 표현합니다.
// 출발점으로부터 동쪽으로 2, 북쪽으로 3만큼 떨어졌다면 [2, 3]을 return 합니다.
// 출발점으로부터 서쪽으로 1, 남쪽으로 4만큼 떨어졌다면 [-1, -4]를 return 합니다.

class Solution {
    public int[] solution(String route) {
        int east = 0;
        int north = 0;
        int[] answer = new int [2];
        for(int i=0; i<route.length(); i++){
            switch(route.charAt(i)){
                case 'N':
                    north++;
                    break;
                case 'S':
                    north--;
                    break;
                case 'E':
                    east++;
                    break;
                case 'W':
                    east--;
                    break;
            }
        }
        answer[0] = east;
        answer[1] = north;
        return answer;
    }
}

// A반 학생들은 시험이 끝난 뒤 성적이 나오기 전 자기 시험지를 가채점해 보았습니다. 이후에 선생님이 실제 성적을 불러 줄 때 가채점한 점수와 실제 성적이 다른 학생들이 있어 선생님께 문의를 하려고 합니다.
// 성적을 문의하려는 학생들의 번호가 담긴 정수 리스트 numbers와 가채점한 점수가 성적을 문의하려는 학생 순서대로 담긴 정수 리스트 our_score, 실제 성적이 번호 순서대로 담긴 정수 리스트 score_list가 주어집니다. 주어진 solution 함수는 가채점한 점수가 실제 성적과 동일하다면 "Same"을, 다르다면 "Different"를 순서대로 리스트에 담아 return하는 함수입니다. solution 함수가 올바르게 작동하도록 한 줄을 수정해 주세요.

class Solution {
    public String[] solution(int[] numbers, int[] our_score, int[] score_list) {
        int num_student = numbers.length;
        String[] answer = new String[num_student];

        for (int i = 0; i < num_student; i++) {
            if (our_score[i] == score_list[numbers[i]-1]) {
                answer[i] = "Same";
            }
            else {
                answer[i] = "Different";
            }
        }

        return answer;
    }
}

// 상우가 사용하는 가습기에는 "auto", "target", "minimum"의 세 가지 모드가 있습니다. 가습기의 가습량은 0~5단계로 구분되며 각 모드 별 동작 방식은 다음과 같습니다.
// "auto" 모드
// 습도가 0 이상 10 미만인 경우 : 5단계
// 습도가 10 이상 20 미만인 경우 : 4단계
// 습도가 20 이상 30 미만인 경우 : 3단계
// 습도가 30 이상 40 미만인 경우 : 2단계
// 습도가 40 이상 50 미만인 경우 : 1단계
// 습도가 50 이상인 경우 : 0단계
// "target" 모드
// 습도가 설정값 미만일 경우 : 3단계
// 습도가 설정값 이상일 경우 : 1단계
// "minimum"모드
// 습도가 설정값 미만일 경우 : 1단계
// 습도가 설정값 이상일 경우 : 0단계
// 상우가 설정한 가습기의 모드를 나타낸 문자열 mode_type, 현재 공기 중 습도를 나타낸 정수 humidity, 설정값을 나타낸 정수 val_set이 주어질 때 현재 가습기가 몇 단계로 작동 중인지 return하도록 빈칸을 채워 solution 함수를 완성해 주세요.

class Solution {
    public int func1(int humidity, int val_set){
        if(humidity < val_set)
            return 3;
        return 1;
    }

    public int func2(int humidity){
        if(humidity >= 50)
            return 0;
        else if (humidity >= 40)
            return 1;
        else if (humidity >= 30)
            return 2;
        else if (humidity >= 20)
            return 3;
        else if (humidity >= 10)
            return 4;       
        else
            return 5;
    }

    public int func3(int humidity, int val_set){
        if(humidity < val_set)
            return 1;
        return 0;
    }

    public int solution(String mode_type, int humidity, int val_set) {
        int answer = 0;

        if(mode_type.equals("auto")){
            answer = func2(humidity);
        }
        else if(mode_type.equals("target")){
            answer = func1(humidity,val_set);
        }
        else if(mode_type.equals("minimum")){
            answer = func3(humidity,val_set);
        }

        return answer;
    }
}

// 선빈이는 게임을 즐기던 중 가지고 있는 물건이 너무 많아 창고 정리를 하기로 했습니다. 선빈이가 보유한 게임 속 창고는 여러 칸으로 나누어져 있고 각 칸에는 물건들이 담겨있습니다. 창고를 정리할 방법을 고민하던 선빈이는 같은 물건이 여러 칸에 나누어 들어있는 것을 발견하고 우선 같은 물건끼리 최대한 겹쳐쌓는 방식으로 창고를 정리하기로 했습니다. 선빈이의 창고에 들어있는 물건의 이름과 개수는 리스트 형태로 주어지며, 한 칸에 겹쳐질 수 있는 물건의 개수에는 제한이 없다고 가정합니다.
// 예를 들어 창고의 각 칸에 담겨있는 물건의 이름이storage = ["pencil", "pencil", "pencil", "book"], 각 물건의 개수가 num = [2, 4, 3, 1]이라면 연필과 책을 한 칸에 각각 겹쳐 쌓아 간단하게 clean_storage = ["pencil", "book"], clean_num = [9, 1]로 만들 수 있습니다.
// pencil book javacpp.jpg
// 주어진 solution 함수는 정리되기 전 창고의 물건 이름이 담긴 문자열 리스트 storage와 각 물건의 개수가 담긴 정수 리스트 num이 주어질 때, 정리된 창고에서 개수가 가장 많은 물건의 이름을 return 하는 함수입니다. solution 함수가 올바르게 작동하도록 한 줄을 수정해 주세요.

class Solution {
    public String solution(String[] storage, int[] num) {
        int num_item = 0;
        String[] clean_storage = new String[storage.length];
        int[] clean_num = new int[num.length];
        
        for(int i=0; i<storage.length; i++){
            int clean_idx = -1;
            for(int j=0; j<num_item; j++){
                if(storage[i].equals(clean_storage[j])){
                    clean_idx = j;
                    break;
                }
            }
            if(clean_idx == -1){
                clean_storage[num_item] = storage[i];
                clean_num[num_item] = num[i];
                num_item += 1;
            }
            else{
                clean_num[clean_idx] += num[i];
            }
        }
        
        // 아래 코드에는 틀린 부분이 없습니다.
        
        int num_max = -1;
        String answer = "";
        for(int i=0; i<num_item; i++){
            if(clean_num[i] > num_max){
                num_max = clean_num[i];
                answer = clean_storage[i];
            }
        }
        return answer;
    }
}