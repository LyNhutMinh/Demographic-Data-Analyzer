import pandas as pd

def calculate_demographic_data(print_data=True):
    # Đọc dữ liệu
    df = pd.read_csv('adult.data.csv')

    # 1. Số lượng người của mỗi chủng tộc (Race)
    race_count = df['race'].value_counts()

    # 2. Độ tuổi trung bình của nam giới (làm tròn 1 chữ số thập phân)
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Phần trăm người có bằng Cử nhân (Bachelors)
    percentage_bachelors = round(len(df[df['education'] == 'Bachelors']) / len(df) * 100, 1)

    # 4. Những người có trình độ cao (Bachelors, Masters, Doctorate)
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Phần trăm thu nhập >50K cho nhóm trình độ cao
    higher_education_rich = round(len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education) * 100, 1)
    
    # Phần trăm thu nhập >50K cho nhóm trình độ thấp
    lower_education_rich = round(len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education) * 100, 1)

    # 5. Số giờ làm việc tối thiểu/tuần
    min_work_hours = df['hours-per-week'].min()

    # 6. Phần trăm người làm giờ tối thiểu có thu nhập >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(len(num_min_workers[num_min_workers['salary'] == '>50K']) / len(num_min_workers) * 100, 1)

    # 7. Quốc gia có tỉ lệ người thu nhập >50K cao nhất
    country_stats = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    highest_earning_country = country_stats['>50K'].idxmax()
    highest_earning_country_percentage = round(country_stats['>50K'].max() * 100, 1)

    # 8. Nghề nghiệp phổ biến nhất của người giàu (>50K) tại Ấn Độ (India)
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # --- KHÔNG THAY ĐỔI PHẦN DƯỚI ĐÂY ---
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Phần này dùng để bạn tự test trực tiếp trong VS Code
if __name__ == '__main__':
    calculate_demographic_data()