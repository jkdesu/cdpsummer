import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch
import time

def create_dual_perspective_animation():
    """Create an animated dual perspective: toy's journey vs bot's transparent view"""
    
    # Set up the figure with two subplots side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
    
    # Left side: Toy's Journey
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 8)
    ax1.set_aspect('equal')
    ax1.set_title("🧸 Toy's Journey Through Supply Chain", fontsize=14, fontweight='bold')
    
    # Right side: Bot's Transparent View
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 8)
    ax2.set_aspect('equal')
    ax2.set_title("🤖 Collector Bot's Transparent View", fontsize=14, fontweight='bold')
    
    # Toy's supply chain stages
    toy_stages = [
        {"name": "Oil (Saudi Arabia)", "pos": (1, 6), "cost": 0.45, "emotion": "😰", "color": "black", "thought": "I'm just black goo..."},
        {"name": "Refining (Singapore)", "pos": (2.5, 6), "cost": 0.53, "emotion": "✨", "color": "gray", "thought": "I'm being transformed!"},
        {"name": "Ethylene (China)", "pos": (4, 6), "cost": 0.08, "emotion": "🤔", "color": "lightblue", "thought": "I'm becoming something new..."},
        {"name": "PVC Creation", "pos": (5.5, 6), "cost": 0.55, "emotion": "😕", "color": "white", "thought": "I'm plastic now..."},
        {"name": "Mold Injection", "pos": (7, 6), "cost": 1.93, "emotion": "😣", "color": "pink", "thought": "I'm being forced into shape!"},
        {"name": "Painting", "pos": (8.5, 6), "cost": 0.08, "emotion": "🎨", "color": "yellow", "thought": "I'm getting my face!"},
        {"name": "Assembly", "pos": (2, 4), "cost": 0.55, "emotion": "😊", "color": "green", "thought": "I have friends!"},
        {"name": "Quality Check", "pos": (4, 4), "cost": 0.08, "emotion": "😰", "color": "orange", "thought": "Am I good enough?"},
        {"name": "Packaging", "pos": (6, 4), "cost": 0.08, "emotion": "🤷‍♂️", "color": "purple", "thought": "I'm being wrapped up..."},
        {"name": "Shipping", "pos": (8, 4), "cost": 0.53, "emotion": "🌍", "color": "blue", "thought": "I'm traveling the world!"},
        {"name": "Store Shelf", "pos": (5, 2), "cost": 0.08, "emotion": "👀", "color": "red", "thought": "I'm on display!"},
        {"name": "Price Discovery", "pos": (5, 0.5), "cost": 745, "emotion": "😱", "color": "darkred", "thought": "Wait... $745? For ME?"}
    ]
    
    # Bot's transparent analysis stages
    bot_stages = [
        {"name": "Watching Toy", "pos": (1, 6), "emotion": "👁️", "color": "gold", "analysis": "Toy starts journey...", "market_price": 0},
        {"name": "Labor Visibility", "pos": (2.5, 6), "emotion": "😰", "color": "orange", "analysis": "I see the workers!", "market_price": 0},
        {"name": "Cost Analysis", "pos": (4, 6), "emotion": "📊", "color": "red", "analysis": "Material: $8.84", "market_price": 0},
        {"name": "Price Shock", "pos": (5.5, 6), "emotion": "😱", "color": "darkred", "analysis": "Market: $745?!", "market_price": 745},
        {"name": "Transparency Impact", "pos": (7, 6), "emotion": "🤔", "color": "purple", "analysis": "Would I still pay this?", "market_price": 745},
        {"name": "Psychology Change", "pos": (8.5, 6), "emotion": "🧠", "color": "cyan", "analysis": "FOMO gone with transparency", "market_price": 745},
        {"name": "Value Question", "pos": (2, 4), "emotion": "❓", "color": "brown", "analysis": "Is it worth $745 now?", "market_price": 745},
        {"name": "Market Doubt", "pos": (4, 4), "emotion": "😤", "color": "darkorange", "analysis": "I won't pay that much!", "market_price": 745},
        {"name": "Price Resistance", "pos": (6, 4), "emotion": "✋", "color": "yellow", "analysis": "Maybe $50 max...", "market_price": 50},
        {"name": "New Pricing", "pos": (8, 4), "emotion": "💰", "color": "green", "analysis": "Fair price: $25", "market_price": 25},
        {"name": "Transparency Effect", "pos": (5, 2), "emotion": "📉", "color": "cyan", "analysis": "Market crashes with transparency", "market_price": 25},
        {"name": "New Reality", "pos": (5, 0.5), "emotion": "🌟", "color": "white", "analysis": "Transparency changes everything", "market_price": 25}
    ]
    
    # Animation variables
    toy_pos = [1, 6]
    toy_emotion = "😰"
    toy_color = "black"
    toy_cost = 0
    
    bot_pos = [1, 6]
    bot_emotion = "👁️"
    bot_color = "gold"
    bot_analysis = "Watching toy's journey..."
    market_price = 0
    
    def animate(frame):
        nonlocal toy_pos, toy_emotion, toy_color, toy_cost
        nonlocal bot_pos, bot_emotion, bot_color, bot_analysis, market_price
        
        # Clear both subplots
        ax1.clear()
        ax2.clear()
        
        # Set up subplots
        ax1.set_xlim(0, 10)
        ax1.set_ylim(0, 8)
        ax1.set_aspect('equal')
        ax1.set_title("🧸 Toy's Journey Through Supply Chain", fontsize=14, fontweight='bold')
        
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.set_aspect('equal')
        ax2.set_title("🤖 Collector Bot's Transparent View", fontsize=14, fontweight='bold')
        
        # Add transparency overlay to bot's view
        overlay = Rectangle((0, 0), 10, 8, facecolor='lightblue', alpha=0.3)
        ax2.add_patch(overlay)
        
        # Draw toy stages (left side)
        for i, stage in enumerate(toy_stages):
            circle = Circle(stage["pos"], 0.3, color=stage["color"], alpha=0.7)
            ax1.add_patch(circle)
            
            ax1.text(stage["pos"][0], stage["pos"][1] + 0.5, stage["name"], 
                    ha='center', va='bottom', fontsize=8, fontweight='bold')
            
            ax1.text(stage["pos"][0], stage["pos"][1] - 0.5, f"${stage['cost']:.2f}", 
                    ha='center', va='top', fontsize=7)
            
            ax1.text(stage["pos"][0], stage["pos"][1], stage["emotion"], 
                    ha='center', va='center', fontsize=16)
        
        # Draw bot stages (right side)
        for i, stage in enumerate(bot_stages):
            circle = Circle(stage["pos"], 0.3, color=stage["color"], alpha=0.7)
            ax2.add_patch(circle)
            
            ax2.text(stage["pos"][0], stage["pos"][1] + 0.5, stage["name"], 
                    ha='center', va='bottom', fontsize=8, fontweight='bold')
            
            ax2.text(stage["pos"][0], stage["pos"][1] - 0.5, f"${stage['market_price']}", 
                    ha='center', va='top', fontsize=7)
            
            ax2.text(stage["pos"][0], stage["pos"][1], stage["emotion"], 
                    ha='center', va='center', fontsize=16)
        
        # Animate toy movement (left side)
        if frame < 120:
            progress = frame / 120
            stage_idx = int(progress * (len(toy_stages) - 1))
            
            if stage_idx < len(toy_stages) - 1:
                start_pos = toy_stages[stage_idx]["pos"]
                end_pos = toy_stages[stage_idx + 1]["pos"]
                
                toy_pos[0] = start_pos[0] + (end_pos[0] - start_pos[0]) * (progress * (len(toy_stages) - 1) - stage_idx)
                toy_pos[1] = start_pos[1] + (end_pos[1] - start_pos[1]) * (progress * (len(toy_stages) - 1) - stage_idx)
                
                toy_emotion = toy_stages[stage_idx]["emotion"]
                toy_color = toy_stages[stage_idx]["color"]
                toy_cost = sum(toy_stages[i]["cost"] for i in range(stage_idx + 1))
                
                # Update bot to match toy's progress
                bot_pos = bot_stages[stage_idx]["pos"]
                bot_emotion = bot_stages[stage_idx]["emotion"]
                bot_color = bot_stages[stage_idx]["color"]
                bot_analysis = bot_stages[stage_idx]["analysis"]
                market_price = bot_stages[stage_idx]["market_price"]
                
            else:
                toy_pos = toy_stages[-1]["pos"]
                toy_emotion = "😱"
                toy_color = "darkred"
                toy_cost = 8.84
                
                bot_pos = bot_stages[-1]["pos"]
                bot_emotion = "🌟"
                bot_color = "white"
                bot_analysis = "Transparency changes everything"
                market_price = 25
        
        # Draw the toy (left side)
        toy_circle = Circle(toy_pos, 0.4, color=toy_color, alpha=0.9, edgecolor='black', linewidth=2)
        ax1.add_patch(toy_circle)
        ax1.text(toy_pos[0], toy_pos[1], toy_emotion, ha='center', va='center', fontsize=20)
        
        # Draw the bot (right side)
        bot_circle = Circle(bot_pos, 0.4, color=bot_color, alpha=0.9, edgecolor='black', linewidth=2)
        ax2.add_patch(bot_circle)
        ax2.text(bot_pos[0], bot_pos[1], bot_emotion, ha='center', va='center', fontsize=20)
        
        # Add journey text (left side)
        ax1.text(0.5, 7.5, f"Toy's Cost: ${toy_cost:.2f}\nToy's Emotion: {toy_emotion}", 
                fontsize=12, fontweight='bold', 
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.8))
        
        # Add analysis text (right side)
        ax2.text(0.5, 7.5, f"Market Price: ${market_price}\nBot Analysis: {bot_analysis}", 
                fontsize=12, fontweight='bold', 
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.8))
        
        # Add dramatic titles at the bottom
        if frame < 120:
            ax1.text(5, 0.2, "🧸 TOY'S INNOCENT JOURNEY 🧸", ha='center', fontsize=12, fontweight='bold')
            ax2.text(5, 0.2, "🤖 BOT'S TRANSPARENT ANALYSIS 🤖", ha='center', fontsize=12, fontweight='bold')
        else:
            ax1.text(5, 0.2, "😱 COLLECTOR DISCOVERS THE TRUTH! 😱", ha='center', fontsize=12, fontweight='bold', color='red')
            ax2.text(5, 0.2, "🌟 BOT'S INSIGHT: ENLIGHTENED! 🌟", ha='center', fontsize=12, fontweight='bold', color='gold')
        
        # Add final comparison
        if frame >= 120:
            ax1.text(0.5, 1.5, f"Material Cost: ${8.84:.2f}\nCollector's Reaction: SHOCKED!", 
                    fontsize=10, fontweight='bold', color='red',
                    bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.9))
            
            ax2.text(0.5, 1.5, f"New Market Price: ${25}\nTransparency Effect: MARKET CRASH!", 
                    fontsize=10, fontweight='bold', color='blue',
                    bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcyan', alpha=0.9))
    
    # Create animation
    anim = animation.FuncAnimation(fig, animate, frames=150, interval=100, repeat=False)
    
    plt.tight_layout()
    plt.show()
    
    return anim

def save_dual_perspective_gif():
    """Save the dual-perspective animation as a GIF"""
    
    print("🎬 Creating dual-perspective GIF...")
    
    # Set up the figure with two subplots side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Toy's journey stages (left side)
    toy_stages = [
        {"name": "Oil (Saudi Arabia)", "pos": (1, 6), "cost": 0.45, "emotion": "😰", "color": "black"},
        {"name": "Refining (Singapore)", "pos": (2.5, 6), "cost": 0.53, "emotion": "✨", "color": "orange"},
        {"name": "Ethylene (China)", "pos": (4, 6), "cost": 0.08, "emotion": "🤔", "color": "yellow"},
        {"name": "PVC Creation", "pos": (5.5, 6), "cost": 0.55, "emotion": "😕", "color": "lightblue"},
        {"name": "Mold Injection", "pos": (7, 6), "cost": 1.93, "emotion": "😣", "color": "pink"},
        {"name": "Painting", "pos": (8.5, 6), "cost": 0.08, "emotion": "🎨", "color": "purple"},
        {"name": "Assembly", "pos": (2, 4), "cost": 0.55, "emotion": "😊", "color": "green"},
        {"name": "Quality Check", "pos": (4, 4), "cost": 0.08, "emotion": "😰", "color": "cyan"},
        {"name": "Packaging", "pos": (6, 4), "cost": 0.08, "emotion": "🤷‍♂️", "color": "brown"},
        {"name": "Shipping", "pos": (8, 4), "cost": 0.53, "emotion": "🌍", "color": "blue"},
        {"name": "Store Shelf", "pos": (5, 2), "cost": 0.08, "emotion": "👀", "color": "lightgreen"},
        {"name": "Price Discovery", "pos": (5, 0.5), "cost": 745, "emotion": "😱", "color": "darkred"}
    ]
    
    # Bot's transparent analysis stages (right side)
    bot_stages = [
        {"name": "Watching Toy", "pos": (1, 6), "emotion": "👁️", "color": "gold", "analysis": "Toy starts journey...", "market_price": 0},
        {"name": "Labor Visibility", "pos": (2.5, 6), "emotion": "😰", "color": "orange", "analysis": "I see the workers!", "market_price": 0},
        {"name": "Cost Analysis", "pos": (4, 6), "emotion": "📊", "color": "red", "analysis": "Material: $8.84", "market_price": 0},
        {"name": "Price Shock", "pos": (5.5, 6), "emotion": "😱", "color": "darkred", "analysis": "Market: $745?!", "market_price": 745},
        {"name": "Transparency Impact", "pos": (7, 6), "emotion": "🤔", "color": "purple", "analysis": "Would I still pay this?", "market_price": 745},
        {"name": "Psychology Change", "pos": (8.5, 6), "emotion": "🧠", "color": "cyan", "analysis": "FOMO gone with transparency", "market_price": 745},
        {"name": "Value Question", "pos": (2, 4), "emotion": "❓", "color": "brown", "analysis": "Is it worth $745 now?", "market_price": 745},
        {"name": "Market Doubt", "pos": (4, 4), "emotion": "😤", "color": "darkorange", "analysis": "I won't pay that much!", "market_price": 745},
        {"name": "Price Resistance", "pos": (6, 4), "emotion": "✋", "color": "yellow", "analysis": "Maybe $50 max...", "market_price": 50},
        {"name": "New Pricing", "pos": (8, 4), "emotion": "💰", "color": "green", "analysis": "Fair price: $25", "market_price": 25},
        {"name": "Transparency Effect", "pos": (5, 2), "emotion": "📉", "color": "cyan", "analysis": "Market crashes with transparency", "market_price": 25},
        {"name": "New Reality", "pos": (5, 0.5), "emotion": "🌟", "color": "white", "analysis": "Transparency changes everything", "market_price": 25}
    ]
    
    # Set up both subplots
    for ax in [ax1, ax2]:
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.set_aspect('equal')
        ax.axis('off')
    
    # Add transparency overlay to right side
    transparency_patch = FancyBboxPatch((0, 0), 10, 8, 
                                       boxstyle="round,pad=0.1", 
                                       facecolor='lightblue', alpha=0.1)
    ax2.add_patch(transparency_patch)
    
    def animate(frame):
        ax1.clear()
        ax2.clear()
        
        # Set up both subplots again
        for ax in [ax1, ax2]:
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 8)
            ax.set_aspect('equal')
            ax.axis('off')
        
        # Add transparency overlay to right side
        transparency_patch = FancyBboxPatch((0, 0), 10, 8, 
                                           boxstyle="round,pad=0.1", 
                                           facecolor='lightblue', alpha=0.1)
        ax2.add_patch(transparency_patch)
        
        # Calculate current stage based on frame
        stage_idx = min(frame // 10, len(toy_stages) - 1)
        
        # Draw toy's journey stages (left side)
        toy_cost = 0
        for i in range(stage_idx + 1):
            stage = toy_stages[i]
            toy_cost += stage["cost"]
            
            # Draw stage circle
            circle = Circle(stage["pos"], 0.3, color=stage["color"], alpha=0.7, edgecolor='black', linewidth=1)
            ax1.add_patch(circle)
            ax1.text(stage["pos"][0], stage["pos"][1], stage["emotion"], ha='center', va='center', fontsize=12)
            
            # Add stage name
            ax1.text(stage["pos"][0], stage["pos"][1] - 0.5, stage["name"], ha='center', va='top', fontsize=8)
            
            # Draw connections
            if i > 0:
                prev_pos = toy_stages[i-1]["pos"]
                ax1.plot([prev_pos[0], stage["pos"][0]], [prev_pos[1], stage["pos"][1]], 'k-', alpha=0.5, linewidth=1)
        
        # Draw bot's analysis stages (right side)
        for i in range(stage_idx + 1):
            stage = bot_stages[i]
            
            # Draw stage circle
            circle = Circle(stage["pos"], 0.3, color=stage["color"], alpha=0.7, edgecolor='black', linewidth=1)
            ax2.add_patch(circle)
            ax2.text(stage["pos"][0], stage["pos"][1], stage["emotion"], ha='center', va='center', fontsize=12)
            
            # Add analysis text
            ax2.text(stage["pos"][0], stage["pos"][1] - 0.5, stage["analysis"], ha='center', va='top', fontsize=8)
            
            # Draw connections
            if i > 0:
                prev_pos = bot_stages[i-1]["pos"]
                ax2.plot([prev_pos[0], stage["pos"][0]], [prev_pos[1], stage["pos"][1]], 'k-', alpha=0.5, linewidth=1)
        
        # Position toy and bot at current stage
        if stage_idx < len(toy_stages):
            toy_pos = toy_stages[stage_idx]["pos"]
            toy_emotion = toy_stages[stage_idx]["emotion"]
            toy_color = toy_stages[stage_idx]["color"]
            toy_cost = sum(toy_stages[i]["cost"] for i in range(stage_idx + 1))
            
            bot_pos = bot_stages[stage_idx]["pos"]
            bot_emotion = bot_stages[stage_idx]["emotion"]
            bot_color = bot_stages[stage_idx]["color"]
            bot_analysis = bot_stages[stage_idx]["analysis"]
            market_price = bot_stages[stage_idx]["market_price"]
            
        else:
            toy_pos = toy_stages[-1]["pos"]
            toy_emotion = "😱"
            toy_color = "darkred"
            toy_cost = 8.84
            
            bot_pos = bot_stages[-1]["pos"]
            bot_emotion = "🌟"
            bot_color = "white"
            bot_analysis = "Transparency changes everything"
            market_price = 25
        
        # Draw the toy (left side)
        toy_circle = Circle(toy_pos, 0.4, color=toy_color, alpha=0.9, edgecolor='black', linewidth=2)
        ax1.add_patch(toy_circle)
        ax1.text(toy_pos[0], toy_pos[1], toy_emotion, ha='center', va='center', fontsize=20)
        
        # Draw the bot (right side)
        bot_circle = Circle(bot_pos, 0.4, color=bot_color, alpha=0.9, edgecolor='black', linewidth=2)
        ax2.add_patch(bot_circle)
        ax2.text(bot_pos[0], bot_pos[1], bot_emotion, ha='center', va='center', fontsize=20)
        
        # Add journey text (left side)
        ax1.text(0.5, 7.5, f"Toy's Cost: ${toy_cost:.2f}\nToy's Emotion: {toy_emotion}", 
                fontsize=12, fontweight='bold', 
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.8))
        
        # Add analysis text (right side)
        ax2.text(0.5, 7.5, f"Market Price: ${market_price}\nBot Analysis: {bot_analysis}", 
                fontsize=12, fontweight='bold', 
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.8))
        
        # Add dramatic titles at the bottom
        if frame < 120:
            ax1.text(5, 0.2, "🧸 TOY'S INNOCENT JOURNEY 🧸", ha='center', fontsize=12, fontweight='bold')
            ax2.text(5, 0.2, "🤖 BOT'S TRANSPARENT ANALYSIS 🤖", ha='center', fontsize=12, fontweight='bold')
        else:
            ax1.text(5, 0.2, "😱 COLLECTOR DISCOVERS THE TRUTH! 😱", ha='center', fontsize=12, fontweight='bold', color='red')
            ax2.text(5, 0.2, "🌟 BOT'S INSIGHT: ENLIGHTENED! 🌟", ha='center', fontsize=12, fontweight='bold', color='gold')
        
        # Add final comparison
        if frame >= 120:
            ax1.text(0.5, 1.5, f"Material Cost: ${8.84:.2f}\nCollector's Reaction: SHOCKED!", 
                    fontsize=10, fontweight='bold', color='red',
                    bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.9))
            
            ax2.text(0.5, 1.5, f"New Market Price: ${25}\nTransparency Effect: MARKET CRASH!", 
                    fontsize=10, fontweight='bold', color='blue',
                    bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcyan', alpha=0.9))
    
    # Create animation and save as GIF
    anim = animation.FuncAnimation(fig, animate, frames=150, interval=100, repeat=False)
    
    # Save as GIF
    try:
        anim.save('toy_bot_dual_perspective.gif', writer='pillow', fps=10)
        print("✅ GIF saved as 'toy_bot_dual_perspective.gif'")
    except Exception as e:
        print(f"❌ Error saving GIF: {e}")
        print("💡 Try installing pillow: pip install pillow")
    
    plt.close()

def create_interactive_dual_perspective():
    """Create an interactive version showing both perspectives"""
    
    print("🧸🤖 DUAL PERSPECTIVE: TOY'S JOURNEY vs BOT'S TRANSPARENT VIEW 🤖🧸")
    print("=" * 80)
    
    toy_stages = [
        {"name": "Oil (Saudi Arabia)", "cost": 0.45, "emotion": "😰", "thought": "I'm just black goo... what am I becoming?"},
        {"name": "Refining (Singapore)", "cost": 0.53, "emotion": "✨", "thought": "I'm being transformed! This is exciting!"},
        {"name": "Ethylene (China)", "cost": 0.08, "emotion": "🤔", "thought": "I'm becoming something new... but what?"},
        {"name": "PVC Creation", "cost": 0.55, "emotion": "😕", "thought": "I'm plastic now... is this who I am?"},
        {"name": "Mold Injection", "cost": 1.93, "emotion": "😣", "thought": "I'm being forced into a shape! This hurts!"},
        {"name": "Painting", "cost": 0.08, "emotion": "🎨", "thought": "I'm getting my face! I'm becoming someone!"},
        {"name": "Assembly", "cost": 0.55, "emotion": "😊", "thought": "I have friends! We're all the same!"},
        {"name": "Quality Check", "cost": 0.08, "emotion": "😰", "thought": "Am I good enough? Will I be chosen?"},
        {"name": "Packaging", "cost": 0.08, "emotion": "🤷‍♂️", "thought": "I'm being wrapped up... where am I going?"},
        {"name": "Shipping", "cost": 0.53, "emotion": "🌍", "thought": "I'm traveling the world! This is amazing!"},
        {"name": "Store Shelf", "cost": 0.08, "emotion": "👀", "thought": "I'm on display! People are looking at me!"},
        {"name": "Price Discovery", "cost": 745, "emotion": "😱", "thought": "Wait... $745? For ME? That can't be right..."}
    ]
    
    bot_stages = [
        {"name": "Watching Toy", "emotion": "👁️", "analysis": "Toy starts journey...", "market_price": 0},
        {"name": "Labor Visibility", "emotion": "😰", "analysis": "I see the workers! Real people made this!", "market_price": 0},
        {"name": "Cost Analysis", "emotion": "📊", "analysis": "Material cost: $8.84", "market_price": 0},
        {"name": "Market Comparison", "emotion": "😱", "analysis": "Market price: $745", "market_price": 745},
        {"name": "Algorithm Detection", "emotion": "🤖", "analysis": "The pricing is artificial! It's all algorithms!", "market_price": 745},
        {"name": "Psychology Analysis", "emotion": "🧠", "analysis": "FOMO + Hype + Social Proof = Price", "market_price": 745},
        {"name": "Emotional Response", "emotion": "😤", "analysis": "I've been manipulated by the system!", "market_price": 745},
        {"name": "Reality Check", "emotion": "😠", "analysis": "How dare they hide this from me!", "market_price": 745},
        {"name": "Value Reassessment", "emotion": "🤝", "analysis": "Maybe I can still love it despite knowing...", "market_price": 745},
        {"name": "Knowledge Power", "emotion": "😌", "analysis": "Knowledge is power. I understand now.", "market_price": 745},
        {"name": "New Perspective", "emotion": "🧠", "analysis": "I see the invisible infrastructure now!", "market_price": 745},
        {"name": "Enlightened Bot", "emotion": "🌟", "analysis": "I am enlightened. I see through all illusions!", "market_price": 745}
    ]
    
    toy_cost = 0
    
    for i in range(len(toy_stages)):
        print(f"\n{'='*40}")
        print(f"STAGE {i+1}: {toy_stages[i]['name']}")
        print(f"{'='*40}")
        
        print(f"🧸 TOY'S PERSPECTIVE:")
        print(f"   Cost: ${toy_stages[i]['cost']:.2f}")
        print(f"   Emotion: {toy_stages[i]['emotion']}")
        print(f"   Thought: '{toy_stages[i]['thought']}'")
        
        toy_cost += toy_stages[i]['cost']
        print(f"   Total Cost: ${toy_cost:.2f}")
        
        print(f"\n🤖 BOT'S TRANSPARENT VIEW:")
        print(f"   Emotion: {bot_stages[i]['emotion']}")
        print(f"   Analysis: '{bot_stages[i]['analysis']}'")
        print(f"   Market Price: ${bot_stages[i]['market_price']}")
        
        if i < len(toy_stages) - 1:
            input("\nPress Enter to continue...")
        else:
            print(f"\n{'='*40}")
            print("🚨 FINAL COMPARISON 🚨")
            print(f"{'='*40}")
            print(f"🧸 Collector's Reality:")
            print(f"   Material Cost: ${8.84:.2f}")
            print(f"   Collector's Reaction: SHOCKED!")
            print(f"   Collector's Emotion: 😱")
            
            print(f"\n🤖 Bot's Enlightenment:")
            print(f"   Market Price: ${745}")
            print(f"   Bot's Status: ENLIGHTENED")
            print(f"   Bot's Emotion: 🌟")
            print(f"   Bot's Insight: 'I see through all illusions!'")

def main():
    """Main function"""
    print("🧸🤖 DUAL PERSPECTIVE ANIMATION")
    print("=" * 50)
    
    choice = input("Choose animation type:\n1. Visual Animation (matplotlib)\n2. Interactive Text Journey\n3. Save as GIF\nEnter choice (1, 2, or 3): ")
    
    if choice == "1":
        print("🎬 Creating visual animation...")
        anim = create_dual_perspective_animation()
        print("✅ Animation completed!")
        
    elif choice == "2":
        print("📖 Starting interactive journey...")
        create_interactive_dual_perspective()
        
    elif choice == "3":
        print("🎬 Creating dual-perspective GIF...")
        save_dual_perspective_gif()
        
    else:
        print("❌ Invalid choice. Running interactive version...")
        create_interactive_dual_perspective()

if __name__ == "__main__":
    main() 