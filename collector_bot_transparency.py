import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch
import time

def create_collector_bot_animation():
    """Create an animated Collector Bot reacting to transparency"""
    
    # Set up the figure
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    
    # Bot's emotional journey through transparency discovery
    stages = [
        {"name": "Normal State", "pos": (1, 6), "emotion": "😍", "thought": "I love my KAWS collection!", "color": "gold", "transparency": 0},
        {"name": "First Transparency", "pos": (2.5, 6), "emotion": "🤔", "thought": "Wait... I can see the factory?", "color": "lightblue", "transparency": 20},
        {"name": "Labor Discovery", "pos": (4, 6), "emotion": "😰", "thought": "Real people made this...", "color": "orange", "transparency": 40},
        {"name": "Cost Breakdown", "pos": (5.5, 6), "emotion": "😱", "thought": "Material cost: $8.84?!", "color": "red", "transparency": 60},
        {"name": "Algorithm Exposure", "pos": (7, 6), "emotion": "😵", "thought": "The pricing is artificial!", "color": "purple", "transparency": 80},
        {"name": "Psychological Crisis", "pos": (8.5, 6), "emotion": "😭", "thought": "My collection is a lie!", "color": "darkred", "transparency": 90},
        {"name": "Reality Check", "pos": (2, 4), "emotion": "😤", "thought": "I've been manipulated!", "color": "brown", "transparency": 95},
        {"name": "Anger Phase", "pos": (4, 4), "emotion": "😠", "thought": "How dare they hide this!", "color": "darkorange", "transparency": 98},
        {"name": "Bargaining", "pos": (6, 4), "emotion": "🤝", "thought": "Maybe I can still love it...", "color": "yellow", "transparency": 99},
        {"name": "Acceptance", "pos": (8, 4), "emotion": "😌", "thought": "Knowledge is power", "color": "green", "transparency": 100},
        {"name": "New Perspective", "pos": (5, 2), "emotion": "🧠", "thought": "I see the invisible now", "color": "cyan", "transparency": 100},
        {"name": "Transformed Bot", "pos": (5, 0.5), "emotion": "🌟", "thought": "I am enlightened", "color": "white", "transparency": 100}
    ]
    
    # Animation variables
    bot_pos = [1, 6]
    bot_emotion = "😍"
    bot_color = "gold"
    current_stage = 0
    transparency_level = 0
    journey_text = ""
    
    def animate(frame):
        nonlocal bot_pos, bot_emotion, bot_color, current_stage, transparency_level, journey_text
        
        ax.clear()
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.set_aspect('equal')
        
        # Draw transparency overlay
        if transparency_level > 0:
            overlay = Rectangle((0, 0), 10, 8, facecolor='lightblue', alpha=transparency_level/100)
            ax.add_patch(overlay)
        
        # Draw stages
        for i, stage in enumerate(stages):
            # Draw stage circle
            circle = Circle(stage["pos"], 0.3, color=stage["color"], alpha=0.7)
            ax.add_patch(circle)
            
            # Add stage name
            ax.text(stage["pos"][0], stage["pos"][1] + 0.5, stage["name"], 
                   ha='center', va='bottom', fontsize=8, fontweight='bold')
            
            # Add thought bubble
            ax.text(stage["pos"][0], stage["pos"][1] - 0.5, stage["thought"], 
                   ha='center', va='top', fontsize=6, style='italic')
            
            # Add emotion
            ax.text(stage["pos"][0], stage["pos"][1], stage["emotion"], 
                   ha='center', va='center', fontsize=16)
        
        # Animate bot movement
        if frame < 120:
            progress = frame / 120
            stage_idx = int(progress * (len(stages) - 1))
            
            if stage_idx < len(stages) - 1:
                start_pos = stages[stage_idx]["pos"]
                end_pos = stages[stage_idx + 1]["pos"]
                
                # Interpolate position
                bot_pos[0] = start_pos[0] + (end_pos[0] - start_pos[0]) * (progress * (len(stages) - 1) - stage_idx)
                bot_pos[1] = start_pos[1] + (end_pos[1] - start_pos[1]) * (progress * (len(stages) - 1) - stage_idx)
                
                # Update bot properties
                bot_emotion = stages[stage_idx]["emotion"]
                bot_color = stages[stage_idx]["color"]
                transparency_level = stages[stage_idx]["transparency"]
                
                # Update journey text
                journey_text = f"Stage {stage_idx + 1}: {stages[stage_idx]['name']}\nTransparency: {transparency_level}%"
                
            else:
                bot_pos = stages[-1]["pos"]
                bot_emotion = "🌟"
                bot_color = "white"
                transparency_level = 100
                journey_text = "ENLIGHTENMENT ACHIEVED!\nBot sees through all illusions!"
        
        # Draw the bot
        bot_circle = Circle(bot_pos, 0.4, color=bot_color, alpha=0.9, edgecolor='black', linewidth=2)
        ax.add_patch(bot_circle)
        ax.text(bot_pos[0], bot_pos[1], bot_emotion, ha='center', va='center', fontsize=20)
        
        # Add journey text
        ax.text(0.5, 7.5, journey_text, fontsize=12, fontweight='bold', 
               bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.8))
        
        # Add dramatic title
        if frame < 120:
            ax.text(5, 7.8, "🤖 COLLECTOR BOT: JOURNEY TO TRANSPARENCY 🤖", 
                   ha='center', fontsize=14, fontweight='bold')
        else:
            ax.text(5, 7.8, "🌟 BOT ACHIEVES ENLIGHTENMENT! 🌟", 
                   ha='center', fontsize=14, fontweight='bold', color='gold')
        
        # Add transparency meter
        if frame >= 120:
            ax.text(0.5, 1.5, f"Transparency Level: {transparency_level}%\nBot Status: ENLIGHTENED\nSees: All hidden processes\nReacts: With full awareness", 
                   fontsize=12, fontweight='bold', color='blue',
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcyan', alpha=0.9))
    
    # Create animation
    anim = animation.FuncAnimation(fig, animate, frames=150, interval=100, repeat=False)
    
    plt.tight_layout()
    plt.show()
    
    return anim

def create_interactive_bot():
    """Create an interactive version where user controls the bot's journey"""
    
    print("🤖 COLLECTOR BOT: JOURNEY TO TRANSPARENCY 🤖")
    print("=" * 60)
    
    stages = [
        {"name": "Normal State", "emotion": "😍", "thought": "I love my KAWS collection! Everything is perfect!", "transparency": 0},
        {"name": "First Transparency", "emotion": "🤔", "thought": "Wait... I can see the factory? That's new...", "transparency": 20},
        {"name": "Labor Discovery", "emotion": "😰", "thought": "Real people made this... I can see their faces!", "transparency": 40},
        {"name": "Cost Breakdown", "emotion": "😱", "thought": "Material cost: $8.84?! But I paid $745!", "transparency": 60},
        {"name": "Algorithm Exposure", "emotion": "😵", "thought": "The pricing is artificial! It's all algorithms!", "transparency": 80},
        {"name": "Psychological Crisis", "emotion": "😭", "thought": "My collection is a lie! Everything I believed is false!", "transparency": 90},
        {"name": "Reality Check", "emotion": "😤", "thought": "I've been manipulated by the system!", "transparency": 95},
        {"name": "Anger Phase", "emotion": "😠", "thought": "How dare they hide this from me!", "transparency": 98},
        {"name": "Bargaining", "emotion": "🤝", "thought": "Maybe I can still love it despite knowing...", "transparency": 99},
        {"name": "Acceptance", "emotion": "😌", "thought": "Knowledge is power. I understand now.", "transparency": 100},
        {"name": "New Perspective", "emotion": "🧠", "thought": "I see the invisible infrastructure now!", "transparency": 100},
        {"name": "Transformed Bot", "emotion": "🌟", "thought": "I am enlightened. I see through all illusions!", "transparency": 100}
    ]
    
    transparency_level = 0
    
    for i, stage in enumerate(stages):
        print(f"\n🤖 Stage {i+1}: {stage['name']}")
        print(f"   Bot's emotion: {stage['emotion']}")
        print(f"   Bot's thought: '{stage['thought']}'")
        print(f"   Transparency level: {stage['transparency']}%")
        
        transparency_level = stage['transparency']
        
        if i < len(stages) - 1:
            input("Press Enter to continue the bot's journey...")
        else:
            print("\n" + "="*60)
            print("🌟 BOT ACHIEVES ENLIGHTENMENT! 🌟")
            print("="*60)
            print(f"Final Transparency Level: {transparency_level}%")
            print(f"Bot Status: ENLIGHTENED")
            print(f"Bot can now see:")
            print(f"- All factory labor processes")
            print(f"- True material costs")
            print(f"- Algorithmic pricing manipulation")
            print(f"- Psychological manipulation tactics")
            print(f"- Hidden supply chain realities")
            print("\n🌟 The Collector Bot is now transformed!")
            print("'I see through all illusions and understand the true nature of hype culture!'")

def main():
    """Main function"""
    print("🤖 COLLECTOR BOT TRANSPARENCY ANIMATION")
    print("=" * 50)
    
    choice = input("Choose animation type:\n1. Visual Animation (matplotlib)\n2. Interactive Text Journey\nEnter choice (1 or 2): ")
    
    if choice == "1":
        print("🎬 Creating visual animation...")
        anim = create_collector_bot_animation()
        print("✅ Animation completed!")
        
    elif choice == "2":
        print("📖 Starting interactive journey...")
        create_interactive_bot()
        
    else:
        print("❌ Invalid choice. Running interactive version...")
        create_interactive_bot()

if __name__ == "__main__":
    main() 