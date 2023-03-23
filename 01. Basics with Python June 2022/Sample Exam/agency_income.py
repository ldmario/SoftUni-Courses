name_airline = input()
quantity_tickets_adult = int(input())
quantity_tickets_children = int(input())
price_ticket_adult_neto = float(input())
tax_service = float(input())

price_ticket_children_neto = price_ticket_adult_neto * 0.3
adult_ticket_with_tax = price_ticket_adult_neto + tax_service
children_ticket_with_tax = price_ticket_children_neto + tax_service
total_profit = ((adult_ticket_with_tax * quantity_tickets_adult) +
                (children_ticket_with_tax * quantity_tickets_children)) * 0.20

print(f"The profit of your agency from {name_airline} tickets is {total_profit:.2f} lv.")
