import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
import os
import time

def create_personalized_dual_perspective_animation():
    """Create an animated dual perspective: toy's journey with personal images vs bot's transparent view"""
    
    # Set up the figure with two subplots side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
    
    # Left side: Toy's Journey with Personal Images
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 8)
    ax1.set_aspect('equal')
    ax1.set_title("🎨 Toy's Journey Through Supply Chain", fontsize=14, fontweight='bold')
    
    # Right side: Bot's Transparent View
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 8)
    ax2.set_aspect('equal')
    ax2.set_title("🤖 Collector Bot's Transparent View", fontsize=14, fontweight='bold')
    
    # Load personal generative images
    generative_images = []
    for i in range(11):  # 0.png through 10.png
        img_path = f"generative/{i}.png"
        if os.path.exists(img_path):
            img = mpimg.imread(img_path)
            generative_images.append(img)
        else:
            print(f"Warning: {img_path} not found")
            # Create a placeholder if image not found
            generative_images.append(None)
    
    # Toy's supply chain stages with personal images
    toy_stages = [
        {"name": "Oil (Saudi Arabia)", "pos": (1, 6), "cost": 0.45, "emotion": "😰", "color": "black", "thought": "I'm just black goo...", "image_idx": 0},
        {"name": "Refining (Singapore)", "pos": (2.5, 6), "cost": 0.53, "emotion": "✨", "color": "gray", "thought": "I'm being transformed!", "image_idx": 1},
        {"name": "Ethylene (China)", "pos": (4, 6), "cost": 0.08, "emotion": "🤔", "color": "lightblue", "thought": "I'm becoming something new...", "image_idx": 2},
        {"name": "PVC Creation", "pos": (5.5, 6), "cost": 0.55, "emotion": "😕", "color": "white", "thought": "I'm plastic now...", "image_idx": 3},
        {"name": "Mold Injection", "pos": (7, 6), "cost": 1.93, "emotion": "😣", "color": "pink", "thought": "I'm being forced into shape!", "image_idx": 4},
        {"name": "Painting", "pos": (8.5, 6), "cost": 0.08, "emotion": "🎨", "color": "yellow", "thought": "I'm getting my face!", "image_idx": 5},
        {"name": "Assembly", "pos": (2, 4), "cost": 0.55, "emotion": "😊", "color": "green", "thought": "I have friends!", "image_idx": 6},
        {"name": "Quality Check", "pos": (4, 4), "cost": 0.08, "emotion": "😰", "color": "orange", "thought": "Am I good enough?", "image_idx": 7},
        {"name": "Packaging", "pos": (6, 4), "cost": 0.08, "emotion": "🤷‍♂️", "color": "purple", "thought": "I'm being wrapped up...", "image_idx": 8},
        {"name": "Shipping", "pos": (8, 4), "cost": 0.53, "emotion": "🌍", "color": "blue", "thought": "I'm traveling the world!", "image_idx": 9},
        {"name": "Store Shelf", "pos": (5, 2), "cost": 0.08, "emotion": "👀", "color": "red", "thought": "I'm on display!", "image_idx": 10},
        {"name": "Price Discovery", "pos": (5, 0.5), "cost": 745, "emotion": "😱", "color": "darkred", "thought": "Wait... $745? For ME?", "image_idx": None}
    ]
    
    # Bot's transparent analysis stages (unchanged)
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
    current_stage = 0
    
    bot_pos = [1, 6]
    bot_emotion = "👁️"
    bot_color = "gold"
    bot_analysis = "Watching toy's journey..."
    market_price = 0
    
    def animate(frame):
        nonlocal toy_pos, toy_emotion, toy_color, toy_cost, current_stage
        nonlocal bot_pos, bot_emotion, bot_color, bot_analysis, market_price
        
        # Clear both subplots
        ax1.clear()
        ax2.clear()
        
        # Set up subplots
        ax1.set_xlim(0, 10)
        ax1.set_ylim(0, 8)
        ax1.set_aspect('equal')
        ax1.set_title("🎨 Toy's Journey Through Supply Chain", fontsize=14, fontweight='bold')
        
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.set_aspect('equal')
        ax2.set_title("🤖 Collector Bot's Transparent View", fontsize=14, fontweight='bold')
        
        # Add transparency overlay to bot's view
        overlay = Rectangle((0, 0), 10, 8, facecolor='lightblue', alpha=0.3)
        ax2.add_patch(overlay)
        
        # Draw toy stages with personal images (left side)
        for i, stage in enumerate(toy_stages):
            # Draw circle background
            circle = Circle(stage["pos"], 0.4, color=stage["color"], alpha=0.7)
            ax1.add_patch(circle)
            
            # Add personal image if available
            if stage["image_idx"] is not None and stage["image_idx"] < len(generative_images) and generative_images[stage["image_idx"]] is not None:
                img = generative_images[stage["image_idx"]]
                # Create image box
                imagebox = OffsetImage(img, zoom=0.15)
                ab = AnnotationBbox(imagebox, stage["pos"], frameon=False)
                ax1.add_artist(ab)
            else:
                # Fallback to emoji if no image
                ax1.text(stage["pos"][0], stage["pos"][1], stage["emotion"], 
                        ha='center', va='center', fontsize=20)
            
            # Add labels
            ax1.text(stage["pos"][0], stage["pos"][1] + 0.6, stage["name"], 
                    ha='center', va='bottom', fontsize=8, fontweight='bold')
            
            ax1.text(stage["pos"][0], stage["pos"][1] - 0.6, f"${stage['cost']:.2f}", 
                    ha='center', va='top', fontsize=7, color='red', fontweight='bold')
        
        # Draw bot stages (right side) - unchanged
        for i, stage in enumerate(bot_stages):
            circle = Circle(stage["pos"], 0.3, color=stage["color"], alpha=0.7)
            ax2.add_patch(circle)
            
            ax2.text(stage["pos"][0], stage["pos"][1], stage["emotion"], 
                    ha='center', va='center', fontsize=16)
            
            ax2.text(stage["pos"][0], stage["pos"][1] + 0.5, stage["name"], 
                    ha='center', va='bottom', fontsize=8, fontweight='bold')
            
            ax2.text(stage["pos"][0], stage["pos"][1] - 0.5, stage["analysis"], 
                    ha='center', va='top', fontsize=7, color='blue', fontweight='bold')
        
        # Animate toy movement
        if frame < len(toy_stages):
            current_stage = frame
            stage = toy_stages[current_stage]
            toy_pos = list(stage["pos"])
            toy_emotion = stage["emotion"]
            toy_color = stage["color"]
            toy_cost = stage["cost"]
        
        # Animate bot movement
        if frame < len(bot_stages):
            stage = bot_stages[frame]
            bot_pos = list(stage["pos"])
            bot_emotion = stage["emotion"]
            bot_color = stage["color"]
            bot_analysis = stage["analysis"]
            market_price = stage["market_price"]
        
        # Draw animated toy (left side)
        if current_stage < len(toy_stages):
            stage = toy_stages[current_stage]
            # Draw moving toy with personal image
            if stage["image_idx"] is not None and stage["image_idx"] < len(generative_images) and generative_images[stage["image_idx"]] is not None:
                img = generative_images[stage["image_idx"]]
                imagebox = OffsetImage(img, zoom=0.2)
                ab = AnnotationBbox(imagebox, toy_pos, frameon=False)
                ax1.add_artist(ab)
            else:
                # Fallback to emoji
                ax1.text(toy_pos[0], toy_pos[1], toy_emotion, 
                        ha='center', va='center', fontsize=24, fontweight='bold')
            
            # Add thought bubble
            ax1.text(toy_pos[0], toy_pos[1] + 0.8, stage["thought"], 
                    ha='center', va='bottom', fontsize=8, 
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
        
        # Draw animated bot (right side)
        ax2.text(bot_pos[0], bot_pos[1], bot_emotion, 
                ha='center', va='center', fontsize=20, fontweight='bold')
        
        # Add bot analysis bubble
        ax2.text(bot_pos[0], bot_pos[1] + 0.8, bot_analysis, 
                ha='center', va='bottom', fontsize=8, 
                bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.8))
        
        # Add market price display
        ax2.text(5, 7.5, f"Market Price: ${market_price}", 
                ha='center', va='center', fontsize=12, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgreen", alpha=0.8))
        
        # Add cost display for toy
        ax2.text(5, 0.5, f"Total Cost: ${toy_cost:.2f}", 
                ha='center', va='center', fontsize=12, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightcoral", alpha=0.8))
    
    # Create animation
    anim = animation.FuncAnimation(fig, animate, frames=len(toy_stages), 
                                 interval=2000, repeat=True, blit=False)
    
    plt.tight_layout()
    plt.show()
    
    return anim

def save_personalized_dual_perspective_gif():
    """Save the personalized dual perspective animation as a GIF"""
    
    # Set up the figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
    
    # Load personal generative images
    generative_images = []
    for i in range(11):
        img_path = f"generative/{i}.png"
        if os.path.exists(img_path):
            img = mpimg.imread(img_path)
            generative_images.append(img)
        else:
            print(f"Warning: {img_path} not found")
            generative_images.append(None)
    
    # Toy's supply chain stages with personal images
    toy_stages = [
        {"name": "Oil (Saudi Arabia)", "pos": (1, 6), "cost": 0.45, "emotion": "😰", "color": "black", "thought": "I'm just black goo...", "image_idx": 0},
        {"name": "Refining (Singapore)", "pos": (2.5, 6), "cost": 0.53, "emotion": "✨", "color": "gray", "thought": "I'm being transformed!", "image_idx": 1},
        {"name": "Ethylene (China)", "pos": (4, 6), "cost": 0.08, "emotion": "🤔", "color": "lightblue", "thought": "I'm becoming something new...", "image_idx": 2},
        {"name": "PVC Creation", "pos": (5.5, 6), "cost": 0.55, "emotion": "😕", "color": "white", "thought": "I'm plastic now...", "image_idx": 3},
        {"name": "Mold Injection", "pos": (7, 6), "cost": 1.93, "emotion": "😣", "color": "pink", "thought": "I'm being forced into shape!", "image_idx": 4},
        {"name": "Painting", "pos": (8.5, 6), "cost": 0.08, "emotion": "🎨", "color": "yellow", "thought": "I'm getting my face!", "image_idx": 5},
        {"name": "Assembly", "pos": (2, 4), "cost": 0.55, "emotion": "😊", "color": "green", "thought": "I have friends!", "image_idx": 6},
        {"name": "Quality Check", "pos": (4, 4), "cost": 0.08, "emotion": "😰", "color": "orange", "thought": "Am I good enough?", "image_idx": 7},
        {"name": "Packaging", "pos": (6, 4), "cost": 0.08, "emotion": "🤷‍♂️", "color": "purple", "thought": "I'm being wrapped up...", "image_idx": 8},
        {"name": "Shipping", "pos": (8, 4), "cost": 0.53, "emotion": "🌍", "color": "blue", "thought": "I'm traveling the world!", "image_idx": 9},
        {"name": "Store Shelf", "pos": (5, 2), "cost": 0.08, "emotion": "👀", "color": "red", "thought": "I'm on display!", "image_idx": 10},
        {"name": "Price Discovery", "pos": (5, 0.5), "cost": 745, "emotion": "😱", "color": "darkred", "thought": "Wait... $745? For ME?", "image_idx": None}
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
    current_stage = 0
    
    bot_pos = [1, 6]
    bot_emotion = "👁️"
    bot_color = "gold"
    bot_analysis = "Watching toy's journey..."
    market_price = 0
    
    def animate(frame):
        nonlocal toy_pos, toy_emotion, toy_color, toy_cost, current_stage
        nonlocal bot_pos, bot_emotion, bot_color, bot_analysis, market_price
        
        # Clear both subplots
        ax1.clear()
        ax2.clear()
        
        # Set up subplots
        ax1.set_xlim(0, 10)
        ax1.set_ylim(0, 8)
        ax1.set_aspect('equal')
        ax1.set_title("🎨 Toy's Journey Through Supply Chain", fontsize=14, fontweight='bold')
        
        ax2.set_xlim(0, 10)
        ax2.set_ylim(0, 8)
        ax2.set_aspect('equal')
        ax2.set_title("🤖 Collector Bot's Transparent View", fontsize=14, fontweight='bold')
        
        # Add transparency overlay to bot's view
        overlay = Rectangle((0, 0), 10, 8, facecolor='lightblue', alpha=0.3)
        ax2.add_patch(overlay)
        
        # Draw toy stages with personal images (left side)
        for i, stage in enumerate(toy_stages):
            # Draw circle background
            circle = Circle(stage["pos"], 0.4, color=stage["color"], alpha=0.7)
            ax1.add_patch(circle)
            
            # Add personal image if available
            if stage["image_idx"] is not None and stage["image_idx"] < len(generative_images) and generative_images[stage["image_idx"]] is not None:
                img = generative_images[stage["image_idx"]]
                # Create image box
                imagebox = OffsetImage(img, zoom=0.15)
                ab = AnnotationBbox(imagebox, stage["pos"], frameon=False)
                ax1.add_artist(ab)
            else:
                # Fallback to emoji if no image
                ax1.text(stage["pos"][0], stage["pos"][1], stage["emotion"], 
                        ha='center', va='center', fontsize=20)
            
            # Add labels
            ax1.text(stage["pos"][0], stage["pos"][1] + 0.6, stage["name"], 
                    ha='center', va='bottom', fontsize=8, fontweight='bold')
            
            ax1.text(stage["pos"][0], stage["pos"][1] - 0.6, f"${stage['cost']:.2f}", 
                    ha='center', va='top', fontsize=7, color='red', fontweight='bold')
        
        # Draw bot stages (right side)
        for i, stage in enumerate(bot_stages):
            circle = Circle(stage["pos"], 0.3, color=stage["color"], alpha=0.7)
            ax2.add_patch(circle)
            
            ax2.text(stage["pos"][0], stage["pos"][1], stage["emotion"], 
                    ha='center', va='center', fontsize=16)
            
            ax2.text(stage["pos"][0], stage["pos"][1] + 0.5, stage["name"], 
                    ha='center', va='bottom', fontsize=8, fontweight='bold')
            
            ax2.text(stage["pos"][0], stage["pos"][1] - 0.5, stage["analysis"], 
                    ha='center', va='top', fontsize=7, color='blue', fontweight='bold')
        
        # Animate toy movement
        if frame < len(toy_stages):
            current_stage = frame
            stage = toy_stages[current_stage]
            toy_pos = list(stage["pos"])
            toy_emotion = stage["emotion"]
            toy_color = stage["color"]
            toy_cost = stage["cost"]
        
        # Animate bot movement
        if frame < len(bot_stages):
            stage = bot_stages[frame]
            bot_pos = list(stage["pos"])
            bot_emotion = stage["emotion"]
            bot_color = stage["color"]
            bot_analysis = stage["analysis"]
            market_price = stage["market_price"]
        
        # Draw animated toy (left side)
        if current_stage < len(toy_stages):
            stage = toy_stages[current_stage]
            # Draw moving toy with personal image
            if stage["image_idx"] is not None and stage["image_idx"] < len(generative_images) and generative_images[stage["image_idx"]] is not None:
                img = generative_images[stage["image_idx"]]
                imagebox = OffsetImage(img, zoom=0.2)
                ab = AnnotationBbox(imagebox, toy_pos, frameon=False)
                ax1.add_artist(ab)
            else:
                # Fallback to emoji
                ax1.text(toy_pos[0], toy_pos[1], toy_emotion, 
                        ha='center', va='center', fontsize=24, fontweight='bold')
            
            # Add thought bubble
            ax1.text(toy_pos[0], toy_pos[1] + 0.8, stage["thought"], 
                    ha='center', va='bottom', fontsize=8, 
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
        
        # Draw animated bot (right side)
        ax2.text(bot_pos[0], bot_pos[1], bot_emotion, 
                ha='center', va='center', fontsize=20, fontweight='bold')
        
        # Add bot analysis bubble
        ax2.text(bot_pos[0], bot_pos[1] + 0.8, bot_analysis, 
                ha='center', va='bottom', fontsize=8, 
                bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.8))
        
        # Add market price display
        ax2.text(5, 7.5, f"Market Price: ${market_price}", 
                ha='center', va='center', fontsize=12, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgreen", alpha=0.8))
        
        # Add cost display for toy
        ax2.text(5, 0.5, f"Total Cost: ${toy_cost:.2f}", 
                ha='center', va='center', fontsize=12, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightcoral", alpha=0.8))
    
    # Create animation
    anim = animation.FuncAnimation(fig, animate, frames=len(toy_stages), 
                                 interval=2000, repeat=True, blit=False)
    
    # Save as GIF
    anim.save('toy_bot_dual_personalized.gif', writer='pillow', fps=0.5)
    print("Personalized dual perspective animation saved as 'toy_bot_dual_personalized.gif'")
    
    plt.close()

def main():
    """Main function to run the personalized dual perspective animation"""
    print("Creating personalized toy-bot dual perspective animation...")
    print("This version uses your generative images (0.png-10.png) for the toy's journey!")
    
    # Check if generative folder exists
    if not os.path.exists("generative"):
        print("Warning: 'generative' folder not found!")
        print("Please create a 'generative' folder with images 0.png through 10.png")
        return
    
    # Check for images
    missing_images = []
    for i in range(11):
        if not os.path.exists(f"generative/{i}.png"):
            missing_images.append(f"{i}.png")
    
    if missing_images:
        print(f"Warning: Missing images: {missing_images}")
        print("The animation will use emojis as fallbacks for missing images.")
    
    # Create and save the animation
    save_personalized_dual_perspective_gif()
    
    # Also create interactive version
    print("\nCreating interactive version...")
    create_personalized_dual_perspective_animation()

if __name__ == "__main__":
    main() 