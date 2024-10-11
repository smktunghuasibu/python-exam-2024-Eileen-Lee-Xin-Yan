# This code contains errors that you need to fix it. Read carefully and do necessary corrections.
# Run the code at online-python.com or IDLE PYTHON before you commit the changes at github.com

# This program is used to calculate compound interest.
# User can input: 
# (a) principal (p), 
# (b) interest rate (r), 
# (c) time in years (t), and 
# (d) number of periods the interest is compounded per year (n)

def cal_matured_value(P, r, t, n):
    result = P * (Pow(1 + ((r / 100) / t), (n * t) / 12 )) 
    return result 

def get_inputs():
    P = float(input("Enter the principal amount: ")) 
    r = float(input("Enter the interest rate: ")) 
    t = float(input("Enter the time in years: ")) 
    n = float(input("Enter the number of periods the interest is compounded per year: ")) 
    return (P, r, t, n) 
    
def main():
    P, R, T, N = get_inputs(P, r, t, n)
    matured_value = cal_matured_value(P, r, t, n)
    print(f"Matured value is { matured_value :.2f}") 

# Don't change the code below!
if __name__ == "__main__":
    main()
