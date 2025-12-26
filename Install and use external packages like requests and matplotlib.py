import matplotlib.pyplot as plt

# Sample Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [10, 15, 7, 22, 18]
expenses = [8, 12, 9, 15, 13]

# Create a figure with a wider size to fit 3 plots
plt.figure(figsize=(15, 5))

# --- Plot 1: Line Chart (Trends) ---
plt.subplot(1, 3, 1) 
plt.plot(months, sales, marker='o', linestyle='-', color='b', label='Sales')
plt.plot(months, expenses, marker='s', linestyle='--', color='r', label='Expenses')
plt.title('Monthly Performance')
plt.xlabel('Month')
plt.ylabel('Value ($)')
plt.legend()
plt.grid(True)

# --- Plot 2: Bar Chart (Comparisons) ---
plt.subplot(1, 3, 2)
plt.bar(months, sales, color='skyblue')
plt.title('Sales Distribution (Bar)')
plt.xlabel('Month')
plt.ylabel('Sales')

# --- Plot 3: Pie Chart (Proportions) ---
plt.subplot(1, 3, 3)
# 'explode' pulls a slice out for emphasis (optional)
explode = (0, 0, 0, 0.1, 0) 
plt.pie(sales, labels=months, autopct='%1.1f%%', startangle=140, explode=explode, colors=plt.cm.Paired.colors)
plt.title('Sales Share by Month')

# Adjust layout so labels don't overlap
plt.tight_layout()

# Display the window
plt.show()
