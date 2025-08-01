import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch
import time

def create_toy_journey_animation():
    """Create an animated journey of a collector discovering toy price psychology"""
    
    # Set up the figure
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    
    # Collector's psychological journey stages
    stages = [
        {"name": "First Sight", "pos": (1, 6), "emotion": "😍", "thought": "OMG it's so cute!", "color": "pink"},
        {"name": "Brand Recognition", "pos": (2.5, 6), "emotion": "🤩", "thought": "It's KAWS! Limited edition!", "color": "gold"},
        {"name": "Social Proof", "pos": (4, 6), "emotion": "👥", "thought": "Everyone wants this!", "color": "blue"},
        {"name": "FOMO Spike", "pos": (5.5, 6), "emotion": "😰", "thought": "What if it sells out?", "color": "red"},
        {"name": "Price Check", "pos": (7, 6), "emotion": "💰", "thought": "Let me see the price...", "color": "green"},
        {"name": "Initial Shock", "pos": (8.5, 6), "emotion": "😱", "thought": "$745?! That's crazy!", "color": "darkred"},
        {"name": "Justification", "pos": (2, 4), "emotion": "🤔", "thought": "But it's an investment...", "color": "orange"},
        {"name": "Comparison", "pos": (4, 4), "emotion": "📊", "thought": "Other collectors pay more", "color": "purple"},
        {"name": "Anchoring", "pos": (6, 4), "emotion": "🎯", "thought": "Original was $2000", "color": "cyan"},
        {"name": "Emotional Attachment", "pos": (8, 4), "emotion": "💕", "thought": "I need this in my life!", "color": "hotpink"},
        {"name": "Purchase Decision", "pos": (5, 2), "emotion": "💳", "thought": "I'm buying it!", "color": "lime"},
        {"name": "Price Discovery", "pos": (5, 0.5), "emotion": "😵", "thought": "Material cost: $8.84", "color": "black"}
    ]
    
    # Animation variables
    collector_pos = [1, 6]  # Start at first sight
    collector_emotion = "😍"
    collector_color = "pink"
    current_stage = 0
    psychology_score = 0
    journey_text = ""
    
    def animate(frame):
        nonlocal collector_pos, collector_emotion, collector_color, current_stage, psychology_score, journey_text
        
        ax.clear()
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.set_aspect('equal')
        
        # Draw psychological journey stages
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
        
        # Animate collector movement
        if frame < 120:  # Journey through psychology
            progress = frame / 120
            stage_idx = int(progress * (len(stages) - 1))
            
            if stage_idx < len(stages) - 1:
                start_pos = stages[stage_idx]["pos"]
                end_pos = stages[stage_idx + 1]["pos"]
                
                # Interpolate position
                collector_pos[0] = start_pos[0] + (end_pos[0] - start_pos[0]) * (progress * (len(stages) - 1) - stage_idx)
                collector_pos[1] = start_pos[1] + (end_pos[1] - start_pos[1]) * (progress * (len(stages) - 1) - stage_idx)
                
                # Update collector properties
                collector_emotion = stages[stage_idx]["emotion"]
                collector_color = stages[stage_idx]["color"]
                psychology_score = (stage_idx + 1) * 10  # Simple psychology score
                
                # Update journey text
                journey_text = f"Stage {stage_idx + 1}: {stages[stage_idx]['name']}\nPsychology Score: {psychology_score}%"
                
            else:  # Final stage - price discovery
                collector_pos = stages[-1]["pos"]
                collector_emotion = "😵"
                collector_color = "black"
                psychology_score = 100
                journey_text = "PRICE DISCOVERY!\nMaterial cost: $8.84\nCollector price: $745\nPsychology drives 98.8% of value!"
        
        # Draw the collector
        collector_circle = Circle(collector_pos, 0.4, color=collector_color, alpha=0.9, edgecolor='black', linewidth=2)
        ax.add_patch(collector_circle)
        ax.text(collector_pos[0], collector_pos[1], collector_emotion, ha='center', va='center', fontsize=20)
        
        # Add journey text
        ax.text(0.5, 7.5, journey_text, fontsize=12, fontweight='bold', 
               bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.8))
        
        # Add dramatic title
        if frame < 120:
            ax.text(5, 7.8, "🧠 COLLECTOR'S PSYCHOLOGICAL JOURNEY TO PRICE DISCOVERY 🧠", 
                   ha='center', fontsize=14, fontweight='bold')
        else:
            ax.text(5, 7.8, "🚨 THE SHOCKING TRUTH ABOUT VALUE! 🚨", 
                   ha='center', fontsize=14, fontweight='bold', color='red')
        
        # Add psychology breakdown at the end
        if frame >= 120:
            ax.text(0.5, 1.5, f"Material Cost: ${8.84:.2f}\nCollector Price: ${745}\nPsychology: 98.8%\nMaterial: 1.2%", 
                   fontsize=12, fontweight='bold', color='red',
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='lightcoral', alpha=0.9))
    
    # Create animation
    anim = animation.FuncAnimation(fig, animate, frames=150, interval=100, repeat=False)
    
    plt.tight_layout()
    plt.show()
    
    return anim

def create_interactive_journey():
    """Create an interactive version where user controls the collector's journey"""
    
    print("🧠 COLLECTOR'S PSYCHOLOGICAL JOURNEY TO PRICE DISCOVERY 🧠")
    print("=" * 60)
    
    stages = [
        {"name": "First Sight", "emotion": "😍", "thought": "OMG it's so cute! I need it!"},
        {"name": "Brand Recognition", "emotion": "🤩", "thought": "It's KAWS! Limited edition! Exclusive!"},
        {"name": "Social Proof", "emotion": "👥", "thought": "Everyone on Instagram has this! It's trending!"},
        {"name": "FOMO Spike", "emotion": "😰", "thought": "What if it sells out? I'll never get another chance!"},
        {"name": "Price Check", "emotion": "💰", "thought": "Let me see the price... please be reasonable..."},
        {"name": "Initial Shock", "emotion": "😱", "thought": "$745?! That's more than my rent! But..."},
        {"name": "Justification", "emotion": "🤔", "thought": "But it's an investment... it will appreciate in value..."},
        {"name": "Comparison", "emotion": "📊", "thought": "Other collectors pay $2000+ for rare pieces..."},
        {"name": "Anchoring", "emotion": "🎯", "thought": "The original was $2000, so $745 is actually a deal!"},
        {"name": "Emotional Attachment", "emotion": "💕", "thought": "I need this in my life! It completes my collection!"},
        {"name": "Purchase Decision", "emotion": "💳", "thought": "I'm buying it! It's worth it for the happiness!"},
        {"name": "Price Discovery", "emotion": "😵", "thought": "Wait... material cost is only $8.84? What am I paying for?"}
    ]
    
    psychology_score = 0
    
    for i, stage in enumerate(stages):
        print(f"\n🧠 Stage {i+1}: {stage['name']}")
        print(f"   Collector's emotion: {stage['emotion']}")
        print(f"   Collector's thought: '{stage['thought']}'")
        
        psychology_score += 10
        print(f"   Psychology score: {psychology_score}%")
        
        if i < len(stages) - 1:
            input("Press Enter to continue the psychological journey...")
        else:
            print("\n" + "="*60)
            print("🚨 THE SHOCKING TRUTH ABOUT VALUE! 🚨")
            print("="*60)
            print(f"Material Cost: ${8.84:.2f}")
            print(f"Collector Price: ${745}")
            print(f"Psychology drives 98.8% of value")
            print(f"Material costs are only 1.2% of price")
            print("\n😵 The collector is having a reality check!")
            print("'I've been paying for psychology, not plastic!'")

def main():
    """Main function"""
    print("🧠 COLLECTOR'S PSYCHOLOGICAL JOURNEY ANIMATION")
    print("=" * 50)
    
    choice = input("Choose animation type:\n1. Visual Animation (matplotlib)\n2. Interactive Text Journey\nEnter choice (1 or 2): ")
    
    if choice == "1":
        print("🎬 Creating visual animation...")
        anim = create_toy_journey_animation()
        print("✅ Animation completed!")
        
    elif choice == "2":
        print("📖 Starting interactive journey...")
        create_interactive_journey()
        
    else:
        print("❌ Invalid choice. Running interactive version...")
        create_interactive_journey()

if __name__ == "__main__":
    main() 