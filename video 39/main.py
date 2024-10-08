import random

questions = [
    ["1. Current Railway Minister of India is ?", "Mamta Banarjee", "Ram Vilash", "Ashwini Vaishnaw", "Piyush Goyal", 2],
    ["2. Which god is also known as 'Gauri Nandan'?", "Agni", "Indra", "Hanuman", "Ganesha", 3],
    ["3. What does not grow on tree according to a popular Hindi saying?", "Money", "Flowers", "Leaves", "Fruits", 0],
    ["4. Which city is known as the Pink City of India?", "Banglore", "Maysore", "Jaipur", "Kochi", 2],
    ["5. Who wrote India's National Anthem?", "Rabindranath Tagore", "Lal Bahadur Shastri", "Chetan Bhagat", "RK Narayan", 0],
    ["6. How many major religions are there in India?", "6", "7", "8", "9", 0],
    ["7. When is the National Hindi Diwas celebrated?", "13 September", "14 September", "14 July", "15 August", 1],
    ["8. How many states are there in India?", "28", "29", "30", "31", 0],
    ["9. Where is India Gate located?", "Agra", "Punjab", "Mumbai", "New Delhi", 3],
    ["10. Who wrote Vande Mataram?", "Sarat Chandra Chattopadhyay", "Rabindranath Tagore", "Bankim Chandra Chatterjee", "Ishwar Chandra Vidyasagar", 2],
    ["11. Which one of the following places is famous for the Great Vishnu Temple?", "Bordubar,Indonesia", "Bamiyan, Afghanistan", "Panja Sahib, Pakistan", "Ankorvat, Cambodia", 3],
    ["12. Where is the largest Buddhist Monastery in India located?", "Sarnath, Uttar Pradesh", "Tawang, Arunachal Pradesh", "Dharmashala, Himachal Pradesh", "Gangtok, Sikkim", 1],
    ["13. Which Indian monument was originally built as a victory tower to commemorate the defeat of the Khan of Khambhat?", "Qutub Minar", "India Gate", "Charminar", "Vijay Stambha", 3],
    ["14. Which ancient civilization is credited with the invention of the first known writing system, cuneiform?", "Egyptians", "Greeks", "Sumerians", "Romans", 2],
    ["15. Which of the following administrative innovations during the Mughal Empire had the most significant long-term impact on the empire's revenue collection system?", "Introduction of the Mansabdari system", "Establishment of the Jagirdari system", "Implementation of Akbar's Dahsala system", "Creation of the Diwan-i-Arz", 2],
    ["16. Who is the founder of the political party Dravida Munnetra Kazhagam (DMK)?", "C.N. Annadurai", "M. Karunanidhi", "M.G. Ramachandran", "Jayalalitha", 0],
    ["17. Who was the first Indian woman to win a medal in the Olympics?", "PT. Usha", "Kunjarani Devi", "Bachendri Pal", "Karnam Maleshwari", 3]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 7500000, 10000000, 75000000]

def play_game():
    money = 0
    guaranteed_money = 0
    for i, question in enumerate(questions):
        print(f"\n\nQuestion for Rs. {levels[i]}")
        print(question[0])
        print(f"a. {question[1]}            b. {question[2]} ")
        print(f"c. {question[3]}            d. {question[4]} ")
        
        reply = input("Enter your answer (a/b/c/d) or q to quit:\n").lower()
        
        if reply == "q":
            final_prize = money 
            print(f"aapne quit karne ka faisla kiya hai to aap yaha se jo dhan rashi leke jaayenge vo hai Rs.\n: , {final_prize}")

            break
        
        if reply not in ['a', 'b', 'c', 'd']:
            print("Invalid input. Please enter 'a', 'b', 'c', or 'd'.")
            continue
        
        answer_index = {'a': 0, 'b': 1, 'c': 2, 'd': 3}[reply]
        
        if answer_index == question[5]:
            print(f"Bilkul sahi jawab, aap jeet chuke hai RS. {levels[i]}")
            money = levels[i]
            if i == 4:
                guaranteed_money = 10000
            elif i == 9:
                guaranteed_money = 320000
            elif i == 14:
                guaranteed_money = 7500000
        else:
            print(F"oho ye galat jawab hai!")
            if 0 <= i <= 3:
                money = 0
            elif 4 <= i <= 8:  # Questions 5 to 9 (index 4 to 8)
                money = 10000
            elif 9 <= i <= 13:  # Questions 10 to 14 (index 9 to 13)
                money = 320000
            elif 14 <= i <= 16:  # Questions 15 to 17 (index 14 to 16)
                money = 7500000
            
    
    final_prize = money 
    print(f"Your take home money is Rs. {final_prize}")

if __name__ == "__main__":
    play_game()


#Answer key 
# 1) C 
# 2) D 
# 3) A 
# 4) C 
# 5) A 
# 6) A 
# 7) B 
# 8) A
# 9) D 
# 10) C  
# 11) D
# 12) B 
# 13) D 
# 14) C 
# 15) C 
# 16) A 
# 17) D
