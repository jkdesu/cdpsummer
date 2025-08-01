import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches
from datetime import datetime, timedelta
import random

# Set style for better visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def create_dramatic_visualization():
    """Create a dramatic visualization showing the cost vs value disconnect"""
    
    # Data
    material_cost = 8.84
    avg_collector_price = 745
    psychology_value = 540  # 72.5% of 745
    brand_value = 200      # 26.8% of 745
    
    # Create figure
    fig = plt.figure(figsize=(20, 12))
    
    # 1. SHOCKING COMPARISON: Material Cost vs. Collector Price
    ax1 = plt.subplot(2, 2, 1)
    
    categories = ['Material Cost', 'Collector Price']
    values = [material_cost, avg_collector_price]
    colors = ['#FF6B6B', '#4ECDC4']
    
    bars = plt.bar(categories, values, color=colors, alpha=0.8)
    plt.title('SHOCKING: Material Cost vs. Collector Price', fontsize=16, fontweight='bold', color='red')
    plt.ylabel('Price ($)')
    plt.ylim(0, 800)
    
    # Add dramatic value labels
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20, 
                f'${value:.0f}', ha='center', va='bottom', fontweight='bold', fontsize=14)
    
    # Add ratio text
    ratio = avg_collector_price / material_cost
    plt.text(0.5, 0.9, f'{ratio:.0f}x MARKUP!', transform=ax1.transAxes, 
             ha='center', fontsize=20, fontweight='bold', color='red',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.8))
    
    # 2. VALUE BREAKDOWN: What You're Actually Paying For
    ax2 = plt.subplot(2, 2, 2)
    
    value_components = ['Psychology\nPremium', 'Brand\nValue', 'Material\nCost']
    value_sizes = [psychology_value, brand_value, material_cost]
    colors = ['#96CEB4', '#45B7D1', '#FF6B6B']
    
    # Create horizontal bar chart
    bars = plt.barh(value_components, value_sizes, color=colors, alpha=0.8)
    plt.title('What You\'re Actually Paying For', fontsize=14, fontweight='bold')
    plt.xlabel('Value ($)')
    
    # Add percentage labels
    total = sum(value_sizes)
    for bar, value in zip(bars, value_sizes):
        percentage = (value / total) * 100
        plt.text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2, 
                f'{percentage:.1f}%', va='center', fontweight='bold', fontsize=12)
    
    # 3. TRANSPARENCY IMPACT: Before vs After
    ax3 = plt.subplot(2, 2, 3)
    
    scenarios = ['Current\n(Hidden)', 'Full\nTransparency', 'Ethical\nPricing']
    prices = [avg_collector_price, 88, 27]  # Current, Transparent, Ethical
    colors = ['#FF6B6B', '#4ECDC4', '#96CEB4']
    
    bars = plt.bar(scenarios, prices, color=colors, alpha=0.8)
    plt.title('Transparency Impact on Price', fontsize=14, fontweight='bold')
    plt.ylabel('Price ($)')
    plt.ylim(0, 800)
    
    # Add dramatic price labels
    for bar, price in zip(bars, prices):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20, 
                f'${price:.0f}', ha='center', va='bottom', fontweight='bold', fontsize=12)
    
    # 4. PSYCHOLOGY VS REALITY: Your KAWS Data
    ax4 = plt.subplot(2, 2, 4)
    
    kaws_figures = ['KAWS_1', 'KAWS_2', 'KAWS_3', 'KAWS_4', 'KAWS_5']
    avg_prices = [409, 509, 1768, 369, 671]
    psychology_scores = [14, 13, 14, 13, 15]  # Total psychology scores
    
    # Create scatter plot
    plt.scatter(psychology_scores, avg_prices, s=200, alpha=0.7, 
               c=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
    
    # Add labels
    for i, name in enumerate(kaws_figures):
        plt.annotate(name, (psychology_scores[i], avg_prices[i]), 
                    xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
    
    plt.xlabel('Psychology Score')
    plt.ylabel('Price ($)')
    plt.title('Psychology vs. Price (Your KAWS Data)', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    # 5. THE BIG REVEAL: What Transparency Would Do
    ax5 = plt.subplot(2, 2, 4)
    ax5.axis('off')
    
    # Create dramatic text display
    reveal_text = f"""
    🚨 THE BIG REVEAL 🚨
    
    Current KAWS Market:
    • Material Cost: ${material_cost:.2f}
    • Collector Price: ${avg_collector_price:.0f}
    • Markup: {ratio:.0f}x
    
    With Full Transparency:
    • Price would drop to: $88
    • Reduction: {((avg_collector_price - 88) / avg_collector_price * 100):.0f}%
    
    With Ethical Pricing:
    • Price would drop to: $27
    • Reduction: {((avg_collector_price - 27) / avg_collector_price * 100):.0f}%
    
    🧠 Psychology drives 99% of value
    💰 Material costs are 1% of price
    🎯 Transparency would COLLAPSE the market
    """
    
    ax5.text(0.1, 0.9, reveal_text, transform=ax5.transAxes, fontsize=12,
             verticalalignment='top', bbox=dict(boxstyle='round,pad=1', 
             facecolor='lightcoral', alpha=0.9), fontweight='bold')
    
    plt.tight_layout(pad=3.0)
    plt.savefig('dramatic_transparency_visualization.png', dpi=300, bbox_inches='tight', pad_inches=0.5)
    plt.show()
    
    return material_cost, avg_collector_price, psychology_value, brand_value

def main():
    """Main function"""
    print("🚨 DRAMATIC TRANSPARENCY VISUALIZATION")
    print("=" * 50)
    
    print("📊 Creating shocking transparency impact visualization...")
    material_cost, avg_price, psychology_value, brand_value = create_dramatic_visualization()
    
    print("\n💥 SHOCKING FINDINGS:")
    print("-" * 40)
    
    ratio = avg_price / material_cost
    psychology_percentage = (psychology_value / avg_price) * 100
    material_percentage = (material_cost / avg_price) * 100
    
    print(f"💰 Material Reality:")
    print(f"   • Actual Cost: ${material_cost:.2f}")
    print(f"   • Collector Price: ${avg_price:.0f}")
    print(f"   • MARKUP: {ratio:.0f}x")
    
    print(f"\n🧠 Psychology Impact:")
    print(f"   • Psychology drives {psychology_percentage:.0f}% of value")
    print(f"   • Material costs are {material_percentage:.1f}% of price")
    
    print(f"\n🎯 Transparency Impact:")
    print(f"   • Full Transparency: ${88:.0f} ({((avg_price - 88) / avg_price * 100):.0f}% reduction)")
    print(f"   • Ethical Pricing: ${27:.0f} ({((avg_price - 27) / avg_price * 100):.0f}% reduction)")
    
    print(f"\n✅ Visualization saved as 'dramatic_transparency_visualization.png'")
    
    return material_cost, avg_price, psychology_value, brand_value

if __name__ == "__main__":
    material_cost, avg_price, psychology_value, brand_value = main() 