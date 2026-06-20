from datetime import date

def is_overdue(due_date, today):
    return due_date < today

def main():
    today = date(2026, 6, 20)
    due_date = date(2026, 6, 18)

    print(is_overdue(due_date, today))

if __name__=="__main__":
    main()