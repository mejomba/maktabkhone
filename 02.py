"""
در گروه B مسابقات جام‌جهانی تیم‌های ایران، پرتغال، اسپانیا و مراکش حضور دارند.
برنامه‌ای بنویسید که با دریافت نتایج بازی‌ها، نام تیم و تعداد برد و باخت و تفاضل گل و امتیاز آن‌ها را به ترتیب در یک خط چاپ کند.
هر تیم به ترتیب امتیاز در یک خط چاپ شود.
 (در صورتی که امتیاز برابر بود، تعداد برد مدنظر قرار گیرد. در صورتی که هم تعداد برد و هم امتیاز برابر بود، بر اساس ترتیب حروف الفبا چاپ شوند.)
نتایج بازی‌ها را به ترتیب زیر بخواند: (در ورودی نمونه عدد سمت چپ مربوط به تیم سمت راست می‌باشد.)
ایران – اسپانیا
ایران – پرتغال
ایران – مراکش
اسپانیا – پرتغال
اسپانیا – مراکش
پرتغال - مراکش
"""

"""
ایران – اسپانیا
ایران – پرتغال
ایران – مراکش
اسپانیا – پرتغال
اسپانیا – مراکش
پرتغال - مراکش
"""
'''
2-2
2-1
1-2
2-2
3-1
2-1
'''


def contest(r, t):
    spain_wins = 0
    spain_lose = 0
    spain_draws = 0
    spain_goal_difference = 0
    spain_points = 0
    iran_wins = 0
    iran_lose = 0
    iran_draws = 0
    iran_goal_difference = 0
    iran_points = 0
    portugal_wins = 0
    portugal_lose = 0
    portugal_draws = 0
    portugal_goal_difference = 0
    portugal_points = 0
    morocco_wins = 0
    morocco_lose = 0
    morocco_draws = 0
    morocco_goal_difference = 0
    morocco_points = 0
    for result_list in r:
        if t[0][0] == 'iran' and t[0][1] == 'spain':
            if int(result_list[0]) == int(result_list[1]):
                iran_draws += 1
                spain_draws += 1
                iran_points += 1
                spain_points += 1
                #iran_goal_difference += 0
                #spain_goal_difference += 0
                #list_result.remove(r[0])
                t.remove(t[0])
            elif int(result_list[0]) > int(result_list[1]):
                iran_wins += 1
                spain_lose += 1
                iran_points += 3
                #spain_points += 0
                iran_goal_difference += int(result_list[0]) - int(result_list[1])
                spain_goal_difference += int(result_list[1]) - int(result_list[0])
                t.remove(t[0])

            elif int(result_list[0]) < int(result_list[1]):
                spain_wins += 1
                iran_lose += 1
                #iran_points += 0
                spain_points += 3
                spain_goal_difference += int(result_list[1]) - int(result_list[0])
                iran_goal_difference += int(result_list[0]) - int(result_list[1])
                t.remove(t[0])

        elif t[0][0] == 'iran' and t[0][1] == 'portugal':
            if int(result_list[0]) == int(result_list[1]):
                iran_draws += 1
                portugal_draws += 1
                portugal_points += 1
                iran_points += 1
                #list_result.remove(r[0])
                t.remove(t[0])
            elif int(result_list[0]) > int(result_list[1]):
                iran_wins += 1
                portugal_lose += 1
                iran_points += 3
                iran_goal_difference += int(result_list[0]) - int(result_list[1])
                portugal_goal_difference += int(result_list[1]) - int(result_list[0])
                #list_result.remove(r[0])
                t.remove(t[0])
            elif int(result_list[0]) < int(result_list[1]):
                portugal_wins += 1
                iran_lose += 1
                portugal_points += 3
                iran_goal_difference += int(result_list[0]) - int(result_list[1])
                portugal_goal_difference += int(result_list[1]) - int(result_list[0])
                #list_result.remove(r[0])
                t.remove(t[0])
        elif t[0][0] == 'iran' and t[0][1] == 'morocco':
            if int(result_list[0]) == int(result_list[1]):
                iran_draws += 1
                morocco_draws += 1
                morocco_points += 1
                iran_points += 1
                #list_result.remove(r[0])
                t.remove(t[0])
            elif int(result_list[0]) > int(result_list[1]):
                iran_wins += 1
                morocco_lose += 1
                iran_points += 3
                iran_goal_difference += int(result_list[0]) - int(result_list[1])
                morocco_goal_difference += int(result_list[1]) - int(result_list[0])
                #list_result.remove(r[0])
                t.remove(t[0])
            elif int(result_list[0]) < int(result_list[1]):
                morocco_wins += 1
                iran_lose += 1
                morocco_points += 3
                iran_goal_difference += int(result_list[0]) - int(result_list[1])
                morocco_goal_difference += int(result_list[1]) - int(result_list[0])
                #list_result.remove(r[0])
                t.remove(t[0])
        elif t[0][0] == 'spain' and t[0][1] == 'portugal':
            if int(result_list[0]) == int(result_list[1]):
                spain_draws += 1
                portugal_draws += 1
                portugal_points += 1
                spain_points += 1
                t.remove(t[0])

            elif int(result_list[0]) > int(result_list[1]):
                spain_wins += 1
                portugal_lose += 1
                spain_points += 3
                spain_goal_difference += int(result_list[0]) - int(result_list[1])
                portugal_goal_difference += int(result_list[1]) - int(result_list[0])
                t.remove(t[0])

            elif int(result_list[0]) < int(result_list[1]):
                portugal_wins += 1
                spain_lose += 1
                portugal_points += 3
                spain_goal_difference += int(result_list[0]) - int(result_list[1])
                portugal_goal_difference += int(result_list[1]) - int(result_list[0])
                t.remove(t[0])

        elif t[0][0] == 'spain' and t[0][1] == 'morocco':
            if int(result_list[0]) == int(result_list[1]):
                spain_draws += 1
                morocco_draws += 1
                morocco_points += 1
                spain_points += 1
                t.remove(t[0])

            elif int(result_list[0]) > int(result_list[1]):
                spain_wins += 1
                morocco_lose += 1
                spain_points += 3
                spain_goal_difference += int(result_list[0]) - int(result_list[1])
                morocco_goal_difference += int(result_list[1]) - int(result_list[0])
                t.remove(t[0])

            elif int(result_list[0]) < int(result_list[1]):
                morocco_wins += 1
                spain_lose += 1
                morocco_points += 3
                spain_goal_difference += int(result_list[0]) - int(result_list[1])
                morocco_goal_difference += int(result_list[1]) - int(result_list[0])
                t.remove(t[0])

        elif t[0][0] == 'portugal' and t[0][1] == 'morocco':
            if int(result_list[0]) == int(result_list[1]):
                portugal_draws += 1
                morocco_draws += 1
                morocco_points += 1
                portugal_points += 1
                t.remove(t[0])
            elif int(result_list[0]) > int(result_list[1]):
                portugal_wins += 1
                morocco_lose += 1
                portugal_points += 3
                portugal_goal_difference += int(result_list[0]) - int(result_list[1])
                morocco_goal_difference += int(result_list[1]) - int(result_list[0])
                t.remove(t[0])
            elif int(result_list[0]) < int(result_list[1]):
                morocco_wins += 1
                portugal_lose += 1
                morocco_points += 3
                morocco_goal_difference += int(result_list[1]) - int(result_list[0])
                portugal_goal_difference += int(result_list[0]) - int(result_list[1])
                t.remove(t[0])

    point_list = [[spain_points, 1, 'Spain', spain_wins, spain_lose, spain_draws, spain_goal_difference],
                  [iran_points, 4, 'Iran', iran_wins, iran_lose, iran_draws, iran_goal_difference],
                  [portugal_points, 2, 'Portugal', portugal_wins, portugal_lose, portugal_draws, portugal_goal_difference],
                  [morocco_points, 3, 'Morocco', morocco_wins, morocco_lose, morocco_draws,morocco_goal_difference]
                  ]
    point_list.sort(reverse=True)
    output = f"""
{(point_list[0][2])} wins:{point_list[0][3]} , loses:{point_list[0][4]} , draws:{point_list[0][5]} , goal difference:{point_list[0][6]} , points:{point_list[0][0]}
{(point_list[1][2])} wins:{point_list[1][3]} , loses:{point_list[1][4]} , draws:{point_list[1][5]} , goal difference:{point_list[1][6]} , points:{point_list[1][0]}
{(point_list[2][2])} wins:{point_list[2][3]} , loses:{point_list[2][4]} , draws:{point_list[2][5]} , goal difference:{point_list[2][6]} , points:{point_list[2][0]}
{(point_list[3][2])} wins:{point_list[3][3]} , loses:{point_list[3][4]} , draws:{point_list[3][5]} , goal difference:{point_list[3][6]} , points:{point_list[3][0]}
"""
    print(output)
list_team = [
    ['iran', 'spain'],
    ['iran', 'portugal'],
    ['iran', 'morocco'],
    ['spain', 'portugal'],
    ['spain', 'morocco'],
    ['portugal', 'morocco']
]

list_result = []
for input_result in range(6):
    result = input()
    list_result.append(result.split('-'))

contest(list_result, list_team)

