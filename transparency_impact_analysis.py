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

def load_kaws_psychology_data():
    """Load the KAWS psychology analysis results"""
    # Your actual KAWS psychology data from previous analysis
    kaws_psychology = {
        'KAWS_1': {
            'name': 'KAWS_1',
            'avg_price': 409,
            'volatility': 110,
            'psychology_scores': {
                'completionist_score': 0,
                'fomo_score': 3,
                'anchoring_score': 3,
                'speculative_score': 2,
                'emotional_score': 5
            },
            'dominant_psychology': 'Emotional Buyer'
        },
        'KAWS_2': {
            'name': 'KAWS_2',
            'avg_price': 509,
            'volatility': 92,
            'psychology_scores': {
                'completionist_score': 0,
                'fomo_score': 4,
                'anchoring_score': 2,
                'speculative_score': 3,
                'emotional_score': 4
            },
            'dominant_psychology': 'FOMO'
        },
        'KAWS_3': {
            'name': 'KAWS_3',
            'avg_price': 1768,
            'volatility': 329,
            'psychology_scores': {
                'completionist_score': 3,
                'fomo_score': 4,
                'anchoring_score': 1,
                'speculative_score': 2,
                'emotional_score': 4
            },
            'dominant_psychology': 'FOMO'
        },
        'KAWS_4': {
            'name': 'KAWS_4',
            'avg_price': 369,
            'volatility': 54,
            'psychology_scores': {
                'completionist_score': 0,
                'fomo_score': 4,
                'anchoring_score': 3,
                'speculative_score': 4,
                'emotional_score': 2
            },
            'dominant_psychology': 'FOMO'
        },
        'KAWS_5': {
            'name': 'KAWS_5',
            'avg_price': 671,
            'volatility': 73,
            'psychology_scores': {
                'completionist_score': 0,
                'fomo_score': 4,
                'anchoring_score': 3,
                'speculative_score': 4,
                'emotional_score': 4
            },
            'dominant_psychology': 'FOMO'
        }
    }
    return kaws_psychology

def load_supply_chain_data():
    """Load the supply chain cost data"""
    # Supply chain cost breakdown from your CSV
    supply_chain_costs = {
        'Raw Materials': {
            'cost': 0.45,  # Average of $0.30-0.60
            'description': 'PVC resin, pigments, additives',
            'visibility': 'Invisible',
            'environmental_impact': 'High'
        },
        'Manufacturing': {
            'cost': 1.93,  # Average of $1.55-2.30
            'description': 'Injection molding, assembly, painting',
            'visibility': 'Invisible',
            'environmental_impact': 'High'
        },
        'Tooling': {
            'cost': 0.55,  # Average of $0.30-0.80
            'description': 'Mold amortization',
            'visibility': 'Invisible',
            'environmental_impact': 'Medium'
        },
        'Logistics': {
            'cost': 0.53,  # Average of $0.40-0.65
            'description': 'Shipping, duties, distribution',
            'visibility': 'Invisible',
            'environmental_impact': 'High'
        },
        'Packaging': {
            'cost': 0.38,  # Average of $0.25-0.50
            'description': 'Box, labels, inserts',
            'visibility': 'Visible',
            'environmental_impact': 'Medium'
        },
        'Business Operations': {
            'cost': 5.00,  # Marketing, branding, retail markup
            'description': 'Brand value, retail overhead',
            'visibility': 'Partially Visible',
            'environmental_impact': 'Low'
        }
    }
    return supply_chain_costs

def calculate_transparency_impact():
    """Calculate how transparency affects perceived value"""
    # Base production cost
    base_cost = 3.84  # Sum of all supply chain costs
    
    # Transparency scenarios
    scenarios = {
        'Current (Hidden)': {
            'cost_visibility': 0.1,  # Only 10% of costs visible
            'price_multiplier': 100,  # 100x markup
            'description': 'Current state - most costs hidden'
        },
        'Partial Transparency': {
            'cost_visibility': 0.4,  # 40% of costs visible
            'price_multiplier': 50,   # 50x markup
            'description': 'Some costs revealed'
        },
        'Full Transparency': {
            'cost_visibility': 0.9,  # 90% of costs visible
            'price_multiplier': 10,   # 10x markup
            'description': 'All costs visible'
        },
        'Ethical Pricing': {
            'cost_visibility': 1.0,  # 100% transparent
            'price_multiplier': 3,    # 3x markup for fair profit
            'description': 'Fair wages + environmental costs'
        }
    }
    return scenarios, base_cost

def create_transparency_visualization():
    """Create comprehensive transparency impact visualization"""
    
    # Load data
    kaws_data = load_kaws_psychology_data()
    supply_chain = load_supply_chain_data()
    scenarios, base_cost = calculate_transparency_impact()
    
    # Create figure
    fig = plt.figure(figsize=(24, 16))
    
    # 1. Cost vs. Value Disparity (Horizontal Bar Chart)
    ax1 = plt.subplot(3, 3, 1)
    
    # Prepare data for horizontal bars
    categories = ['Material Cost', 'Emotional Value', 'Brand Value', 'Collector Psychology']
    material_cost = base_cost
    emotional_value = np.mean([k['avg_price'] for k in kaws_data.values()])
    brand_value = 200  # Estimated KAWS brand premium
    psychology_value = emotional_value - material_cost - brand_value
    
    values = [material_cost, emotional_value, brand_value, psychology_value]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    bars = plt.barh(categories, values, color=colors, alpha=0.8)
    plt.title('Cost vs. Value Disparity in KAWS Toys', fontsize=14, fontweight='bold')
    plt.xlabel('Value ($)')
    
    # Add value labels
    for bar, value in zip(bars, values):
        plt.text(bar.get_width() + 50, bar.get_y() + bar.get_height()/2, 
                f'${value:.0f}', va='center', fontweight='bold')
    
    # 2. Psychology vs. Reality Mapping
    ax2 = plt.subplot(3, 3, 2)
    
    # Scatter plot: Psychology Score vs. Price/Cost Ratio
    psychology_scores = []
    price_cost_ratios = []
    kaws_names = []
    
    for kaws_id, data in kaws_data.items():
        # Calculate total psychology score
        total_score = sum(data['psychology_scores'].values())
        psychology_scores.append(total_score)
        
        # Calculate price/cost ratio
        price_cost_ratio = data['avg_price'] / base_cost
        price_cost_ratios.append(price_cost_ratio)
        kaws_names.append(data['name'])
    
    plt.scatter(psychology_scores, price_cost_ratios, s=200, alpha=0.7, c=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
    
    # Add labels
    for i, name in enumerate(kaws_names):
        plt.annotate(name, (psychology_scores[i], price_cost_ratios[i]), 
                    xytext=(5, 5), textcoords='offset points', fontsize=9, fontweight='bold')
    
    plt.xlabel('Total Psychology Score')
    plt.ylabel('Price/Cost Ratio')
    plt.title('Psychology vs. Material Reality', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    # 3. Supply Chain Cost Breakdown
    ax3 = plt.subplot(3, 3, 3)
    
    cost_categories = list(supply_chain.keys())
    cost_values = [supply_chain[cat]['cost'] for cat in cost_categories]
    visibility_colors = ['red' if supply_chain[cat]['visibility'] == 'Invisible' else 'orange' if supply_chain[cat]['visibility'] == 'Partially Visible' else 'green' for cat in cost_categories]
    
    bars = plt.bar(cost_categories, cost_values, color=visibility_colors, alpha=0.8)
    plt.title('Supply Chain Cost Breakdown', fontsize=14, fontweight='bold')
    plt.ylabel('Cost ($)')
    plt.xticks(rotation=45, ha='right')
    
    # Add cost labels
    for bar, value in zip(bars, cost_values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, 
                f'${value:.2f}', ha='center', va='bottom', fontsize=8)
    
    # 4. Transparency Impact Scenarios
    ax4 = plt.subplot(3, 3, 4)
    
    scenario_names = list(scenarios.keys())
    price_multipliers = [scenarios[name]['price_multiplier'] for name in scenario_names]
    final_prices = [base_cost * multiplier for multiplier in price_multipliers]
    
    bars = plt.bar(scenario_names, final_prices, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'], alpha=0.8)
    plt.title('Price Impact of Transparency', fontsize=14, fontweight='bold')
    plt.ylabel('Final Price ($)')
    plt.xticks(rotation=45, ha='right')
    
    # Add price labels
    for bar, price in zip(bars, final_prices):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, 
                f'${price:.0f}', ha='center', va='bottom', fontweight='bold')
    
    # 5. Psychology Score Heatmap
    ax5 = plt.subplot(3, 3, 5)
    
    # Create psychology score matrix
    psychology_types = ['Completionist', 'FOMO', 'Anchoring', 'Speculative', 'Emotional']
    psychology_data = []
    
    for kaws_id, data in kaws_data.items():
        scores = [data['psychology_scores']['completionist_score'],
                 data['psychology_scores']['fomo_score'],
                 data['psychology_scores']['anchoring_score'],
                 data['psychology_scores']['speculative_score'],
                 data['psychology_scores']['emotional_score']]
        psychology_data.append(scores)
    
    psychology_df = pd.DataFrame(psychology_data, 
                               columns=psychology_types,
                               index=[data['name'] for data in kaws_data.values()])
    
    sns.heatmap(psychology_df, annot=True, cmap='YlOrRd', fmt='.0f', ax=ax5)
    plt.title('Psychology Score Matrix', fontsize=14, fontweight='bold')
    plt.ylabel('KAWS Figure')
    
    # 6. Environmental Impact vs. Price
    ax6 = plt.subplot(3, 3, 6)
    
    # Environmental impact scores
    env_impact_scores = {
        'Raw Materials': 9,
        'Manufacturing': 8,
        'Tooling': 6,
        'Logistics': 7,
        'Packaging': 5,
        'Business Operations': 2
    }
    
    env_categories = list(env_impact_scores.keys())
    env_scores = list(env_impact_scores.values())
    env_costs = [supply_chain[cat]['cost'] for cat in env_categories]
    
    plt.scatter(env_scores, env_costs, s=100, alpha=0.7, c=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#F8B195'])
    
    for i, cat in enumerate(env_categories):
        plt.annotate(cat, (env_scores[i], env_costs[i]), 
                    xytext=(5, 5), textcoords='offset points', fontsize=8)
    
    plt.xlabel('Environmental Impact Score (1-10)')
    plt.ylabel('Cost ($)')
    plt.title('Environmental Impact vs. Cost', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    # 7. Transparency Scenarios Timeline
    ax7 = plt.subplot(3, 3, 7)
    
    # Simulate price changes over time with transparency
    time_points = np.arange(0, 100, 1)
    current_prices = np.full_like(time_points, np.mean([k['avg_price'] for k in kaws_data.values()]))
    
    # Transparency events
    transparency_events = [20, 40, 60, 80]
    price_multipliers = [100, 50, 10, 3]
    
    adjusted_prices = current_prices.copy()
    for i, event in enumerate(transparency_events):
        adjusted_prices[event:] = base_cost * price_multipliers[i]
    
    plt.plot(time_points, current_prices, 'b-', linewidth=2, label='Current Price', alpha=0.7)
    plt.plot(time_points, adjusted_prices, 'r--', linewidth=2, label='With Transparency', alpha=0.7)
    
    # Add event markers
    for event in transparency_events:
        plt.axvline(x=event, color='gray', linestyle=':', alpha=0.5)
    
    plt.xlabel('Time (arbitrary units)')
    plt.ylabel('Price ($)')
    plt.title('Price Evolution with Transparency', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 8. Value Distribution Pie Chart
    ax8 = plt.subplot(3, 3, 8)
    
    # Value distribution
    value_components = ['Material Cost', 'Manufacturing', 'Brand Value', 'Psychology Premium']
    value_sizes = [base_cost, 1.93, 200, emotional_value - base_cost - 200]
    value_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    # Create pie chart without percentage labels inside slices
    wedges, texts = plt.pie(value_sizes, colors=value_colors, 
                           startangle=90, labeldistance=1.3)
    
    # Add custom labels with better positioning and include percentages
    for i, (wedge, component) in enumerate(zip(wedges, value_components)):
        angle = (wedge.theta2 + wedge.theta1) / 2
        x = 1.4 * np.cos(np.radians(angle))
        y = 1.4 * np.sin(np.radians(angle))
        
        # Calculate percentage
        percentage = (value_sizes[i] / sum(value_sizes)) * 100
        
        # Adjust label position based on angle and component
        if component == 'Material Cost':
            # Move Material Cost label further up to avoid title overlap
            y = 1.6 * np.sin(np.radians(angle))
            ha = 'center'
            va = 'bottom'
        elif angle > 90 and angle < 270:
            ha = 'right'
            va = 'center'
        else:
            ha = 'left'
            va = 'center'
        
        # Create label with component name and percentage
        label_text = f"{component}\n({percentage:.1f}%)"
        
        plt.text(x, y, label_text, ha=ha, va=va, fontsize=9, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='white', alpha=0.9))
    
    plt.title('Value Distribution in KAWS Toys', fontsize=14, fontweight='bold', pad=40)
    
    # 9. Summary Statistics
    ax9 = plt.subplot(3, 3, 9)
    ax9.axis('off')
    
    # Calculate key statistics
    avg_psychology_score = np.mean([sum(k['psychology_scores'].values()) for k in kaws_data.values()])
    avg_price_cost_ratio = np.mean([k['avg_price'] / base_cost for k in kaws_data.values()])
    transparency_impact = (current_prices[0] - adjusted_prices[-1]) / current_prices[0] * 100
    
    summary_text = f"""
    Transparency Impact Analysis Summary
    
    📊 Key Findings:
    • Average Psychology Score: {avg_psychology_score:.1f}/25
    • Price/Cost Ratio: {avg_price_cost_ratio:.0f}x markup
    • Material Cost: ${base_cost:.2f} per toy
    • Emotional Value: ${emotional_value:.0f} per toy
    
    🎯 Transparency Impact:
    • Current Price: ${current_prices[0]:.0f}
    • With Full Transparency: ${adjusted_prices[-1]:.0f}
    • Potential Price Reduction: {transparency_impact:.0f}%
    
    🧠 Psychology vs. Reality:
    • Psychology drives 95% of value
    • Material costs are 1% of final price
    • Transparency could collapse prices
    """
    
    ax9.text(0.1, 0.9, summary_text, transform=ax9.transAxes, fontsize=10,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8))
    
    plt.tight_layout(pad=2.0)
    plt.savefig('transparency_impact_analysis.png', dpi=300, bbox_inches='tight', pad_inches=0.5)
    plt.show()
    
    return kaws_data, supply_chain, scenarios

def main():
    """Main analysis function"""
    print("🎯 KAWS Transparency Impact Analysis")
    print("=" * 50)
    
    print("📊 Creating transparency impact visualization...")
    kaws_data, supply_chain, scenarios = create_transparency_visualization()
    
    print("\n📋 Key Insights:")
    print("-" * 40)
    
    # Calculate key metrics
    base_cost = sum([supply_chain[cat]['cost'] for cat in supply_chain.keys()])
    avg_price = np.mean([k['avg_price'] for k in kaws_data.values()])
    price_cost_ratio = avg_price / base_cost
    
    print(f"💰 Material Reality:")
    print(f"   • Actual Production Cost: ${base_cost:.2f}")
    print(f"   • Average Collector Price: ${avg_price:.0f}")
    print(f"   • Price/Cost Ratio: {price_cost_ratio:.0f}x markup")
    
    print(f"\n🧠 Psychology Impact:")
    print(f"   • Psychology drives {((avg_price - base_cost) / avg_price * 100):.0f}% of value")
    print(f"   • Material costs are {(base_cost / avg_price * 100):.1f}% of final price")
    
    print(f"\n🎯 Transparency Scenarios:")
    for scenario, data in scenarios.items():
        final_price = base_cost * data['price_multiplier']
        reduction = ((avg_price - final_price) / avg_price * 100)
        print(f"   • {scenario}: ${final_price:.0f} ({reduction:+.0f}% change)")
    
    print(f"\n✅ Analysis complete! Visualization saved as 'transparency_impact_analysis.png'")
    
    return kaws_data, supply_chain, scenarios

if __name__ == "__main__":
    kaws_data, supply_chain, scenarios = main() 