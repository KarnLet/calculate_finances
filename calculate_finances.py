def calculate_finances(monthly_income: float, tax_rate: float, currency: str) -> None:
    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax

    print('---------------------------------------')
    print(f'Renda mensal: {currency}{monthly_income:,.2f}')
    print(f'Taxa de imposto: {tax_rate:.0f}%')
    print(f'Imposto mensal: {currency}{monthly_tax:,.2f}')
    print(f'Renda líquida mensal: {currency}{monthly_net_income:,.2f}')
    print(f'Salário anual: {currency}{yearly_salary:,.2f}')
    print(f'Imposto anual: {currency}{yearly_tax:,.2f}')
    print(f'Renda líquida anual: {currency}{yearly_net_income:,.2f}')
    print('---------------------------------------')


def main() -> None:
    monthly_income: float = float(input('Digite sua renda mensal: '))
    tax_rate: float = float(input('Digite sua taxa de imposto: '))

    calculate_finances(monthly_income, tax_rate, currency='R$')


if __name__ == '__main__':
    main()