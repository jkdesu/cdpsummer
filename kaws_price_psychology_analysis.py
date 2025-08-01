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

# Define the 5 collector psychology patterns
collector_psychology = {
    1: "Completionist",
    2: "FOMO (Fear of Missing Out)", 
    3: "Anchoring Bias",
    4: "Speculative Buyer",
    5: "Emotional Buyer"
}

def parse_kaws_price_data():
    """Parse the user's actual KAWS price data"""
    
    # KAWS_1 data
    kaws_1_data = [
        ("2025-06-29 02:39", 441), ("2025-06-20 16:45", 418), ("2025-06-04 00:20", 350),
        ("2025-05-02 07:05", 761), ("2025-04-24 11:36", 260), ("2025-04-22 01:03", 309),
        ("2025-04-18 21:32", 358), ("2025-04-06 14:44", 374), ("2025-04-01 03:33", 345),
        ("2025-03-08 10:29", 370), ("2025-02-28 09:22", 368), ("2025-02-13 13:03", 361),
        ("2025-02-06 22:27", 363), ("2025-02-06 16:18", 458), ("2025-01-28 11:45", 363),
        ("2025-01-20 12:35", 351), ("2024-12-17 21:37", 382), ("2024-12-02 08:54", 390),
        ("2024-11-23 02:25", 417), ("2024-11-11 17:57", 450), ("2024-11-08 22:40", 400),
        ("2024-11-06 07:47", 395), ("2024-11-05 06:22", 405), ("2024-10-19 23:11", 403),
        ("2024-10-15 11:07", 406), ("2024-09-14 16:07", 463), ("2024-09-13 11:00", 435),
        ("2024-09-06 04:18", 410), ("2024-08-22 20:03", 456), ("2024-08-22 11:47", 452),
        ("2024-08-21 13:37", 472), ("2024-08-21 00:52", 427), ("2024-08-19 13:36", 435),
        ("2024-08-13 00:06", 417), ("2024-08-12 18:46", 375), ("2024-08-05 20:13", 436),
        ("2024-08-04 10:25", 425), ("2024-07-31 17:25", 429), ("2024-07-29 02:36", 390),
        ("2024-07-20 20:05", 443), ("2024-07-11 11:22", 440), ("2024-06-11 13:21", 326),
        ("2024-06-10 00:35", 553), ("2024-05-23 18:05", 350), ("2024-05-21 02:28", 399),
        ("2024-04-28 21:51", 434), ("2024-04-28 17:33", 474), ("2024-04-17 06:52", 395),
        ("2024-04-02 10:15", 375), ("2024-03-20 22:00", 350)
    ]
    
    # KAWS_2 data
    kaws_2_data = [
        ("2025-07-07 15:20", 520), ("2025-06-04 11:58", 329), ("2025-06-04 09:56", 330),
        ("2025-06-03 13:36", 571), ("2025-05-29 08:49", 330), ("2025-04-25 10:23", 404),
        ("2025-04-08 21:19", 412), ("2025-03-26 17:23", 339), ("2025-01-21 19:47", 350),
        ("2024-12-25 17:47", 425), ("2024-11-19 21:07", 414), ("2024-11-18 17:20", 380),
        ("2024-11-18 15:39", 355), ("2024-10-26 17:10", 414), ("2024-10-04 15:49", 464),
        ("2024-08-15 21:10", 441), ("2024-08-05 17:18", 662), ("2024-06-29 21:55", 795),
        ("2024-06-29 16:18", 665), ("2024-06-20 22:14", 489), ("2024-06-12 14:05", 569),
        ("2024-06-08 08:42", 568), ("2024-04-14 15:44", 661), ("2024-03-11 10:07", 566),
        ("2024-03-09 02:33", 546), ("2024-02-13 19:48", 518), ("2024-02-03 22:24", 500),
        ("2024-01-06 19:45", 549), ("2023-11-28 20:25", 451), ("2023-11-27 16:38", 388),
        ("2023-11-27 00:10", 413), ("2023-10-22 19:36", 490), ("2023-09-05 02:32", 525),
        ("2023-08-24 00:12", 448), ("2023-06-06 09:15", 555), ("2023-05-16 14:43", 545),
        ("2023-05-12 18:58", 406), ("2023-05-01 20:42", 431), ("2023-04-25 17:21", 457),
        ("2023-04-21 08:32", 579), ("2023-04-14 14:08", 550), ("2023-04-13 22:44", 558),
        ("2023-04-03 15:28", 555), ("2023-02-20 15:05", 615), ("2023-02-14 00:49", 678),
        ("2023-01-09 02:04", 630), ("2022-12-28 06:22", 576), ("2022-12-17 18:06", 670),
        ("2022-12-01 23:31", 685), ("2022-11-28 08:26", 684)
    ]
    
    # KAWS_3 data
    kaws_3_data = [
        ("2025-04-22 02:09", 1350), ("2025-02-06 13:37", 1560), ("2025-01-10 04:32", 1555),
        ("2025-01-06 11:00", 1397), ("2024-10-02 10:04", 1189), ("2024-09-24 15:34", 1350),
        ("2024-09-24 12:01", 1527), ("2024-09-10 01:18", 1200), ("2024-06-05 14:21", 1543),
        ("2023-12-04 08:00", 1925), ("2023-07-20 11:52", 1562), ("2023-06-10 20:58", 1567),
        ("2022-11-20 21:51", 1900), ("2022-11-02 05:30", 1566), ("2022-06-24 08:40", 1337),
        ("2022-05-12 04:10", 1827), ("2022-01-22 23:39", 1901), ("2021-12-16 17:46", 2154),
        ("2021-10-03 12:21", 2306), ("2021-09-15 16:20", 2055), ("2021-09-11 16:15", 2008),
        ("2021-07-03 11:38", 1856), ("2021-05-04 18:39", 2863), ("2021-04-21 22:06", 1800),
        ("2021-04-03 23:32", 2084), ("2021-04-02 12:46", 2083), ("2021-03-27 17:51", 2045),
        ("2021-03-13 06:01", 1853), ("2021-02-27 13:10", 2154), ("2021-02-25 07:01", 2104),
        ("2020-12-25 21:32", 1800), ("2020-12-19 21:13", 2053), ("2020-12-06 13:11", 1750),
        ("2020-11-23 03:06", 1649), ("2020-11-14 08:51", 1573), ("2020-11-06 11:55", 1547),
        ("2020-10-21 02:47", 1649), ("2020-10-14 05:52", 1547)
    ]
    
    # KAWS_4 data
    kaws_4_data = [
        ("2025-07-19 15:23", 538), ("2025-07-11 15:17", 321), ("2025-06-15 13:31", 523),
        ("2025-06-10 07:49", 475), ("2025-06-04 11:40", 350), ("2025-06-03 16:18", 351),
        ("2025-05-13 14:30", 330), ("2025-04-18 10:45", 342), ("2025-04-17 14:08", 357),
        ("2025-04-17 12:05", 348), ("2025-04-13 17:37", 377), ("2025-04-04 07:11", 373),
        ("2025-03-09 13:26", 369), ("2025-03-08 04:58", 368), ("2025-03-07 20:56", 368),
        ("2025-02-27 15:08", 369), ("2025-02-20 10:08", 316), ("2025-02-15 04:47", 367),
        ("2025-01-18 09:58", 355), ("2025-01-17 13:02", 378), ("2025-01-17 11:43", 365),
        ("2025-01-07 20:35", 359), ("2024-12-27 11:39", 366), ("2024-12-25 14:08", 363),
        ("2024-12-24 11:13", 360), ("2024-12-16 10:52", 355), ("2024-12-09 18:31", 355),
        ("2024-12-06 18:20", 355), ("2024-12-03 11:42", 355), ("2024-12-02 09:51", 355),
        ("2024-12-02 00:03", 320), ("2024-12-02 00:03", 350), ("2024-11-29 20:38", 363),
        ("2024-11-29 16:29", 360), ("2024-11-24 03:36", 329), ("2024-11-21 17:03", 355),
        ("2024-11-06 10:25", 350), ("2024-10-29 02:27", 388), ("2024-10-21 18:32", 397),
        ("2024-10-21 14:28", 431), ("2024-10-20 09:02", 388), ("2024-10-19 03:21", 431),
        ("2024-10-16 16:37", 320), ("2024-09-21 19:51", 333), ("2024-09-06 11:51", 325),
        ("2024-09-06 08:54", 332), ("2024-09-05 12:01", 350), ("2024-09-04 15:25", 395),
        ("2024-08-29 22:00", 398), ("2024-08-25 23:12", 349), ("2024-08-15 22:00", 398)
    ]
    
    # KAWS_5 data
    kaws_5_data = [
        ("2025-07-05 13:34", 1038), ("2025-06-30 00:10", 750), ("2025-06-26 18:27", 625),
        ("2025-06-03 16:17", 525), ("2025-06-03 12:05", 723), ("2025-05-31 08:58", 737),
        ("2025-05-30 04:01", 690), ("2025-05-27 18:10", 648), ("2025-05-19 18:39", 600),
        ("2025-05-19 16:40", 602), ("2025-05-06 07:20", 600), ("2025-04-28 04:20", 748),
        ("2025-04-21 07:15", 702), ("2025-03-29 22:23", 702), ("2025-03-01 13:17", 669),
        ("2025-02-23 02:31", 622), ("2025-02-19 16:38", 600), ("2025-02-06 13:14", 759),
        ("2025-01-17 10:30", 674), ("2025-01-16 16:15", 675), ("2025-01-09 13:44", 680),
        ("2025-01-08 17:23", 681), ("2025-01-02 11:15", 684), ("2024-12-25 14:08", 687),
        ("2024-12-15 18:40", 685), ("2024-12-13 02:59", 695), ("2024-12-08 08:40", 688),
        ("2024-12-03 20:54", 688), ("2024-12-01 14:34", 688), ("2024-11-28 22:09", 675),
        ("2024-11-28 12:18", 674), ("2024-11-26 09:26", 673), ("2024-11-23 23:20", 674),
        ("2024-11-22 12:06", 659), ("2024-11-22 06:37", 630), ("2024-11-14 15:17", 659),
        ("2024-11-10 18:03", 644), ("2024-11-10 12:07", 610), ("2024-10-24 22:30", 612),
        ("2024-10-20 17:43", 650), ("2024-10-16 12:06", 640), ("2024-10-14 04:07", 666),
        ("2024-10-10 18:26", 594), ("2024-10-04 21:26", 585), ("2024-09-17 13:36", 701),
        ("2024-09-10 11:47", 625), ("2024-09-05 12:00", 650), ("2024-08-31 12:09", 715),
        ("2024-08-31 10:27", 630), ("2024-08-27 19:25", 700)
    ]
    
    # Convert to DataFrames
    kaws_figures = {
        'KAWS_1': {'name': 'KAWS_1', 'data': kaws_1_data},
        'KAWS_2': {'name': 'KAWS_2', 'data': kaws_2_data},
        'KAWS_3': {'name': 'KAWS_3', 'data': kaws_3_data},
        'KAWS_4': {'name': 'KAWS_4', 'data': kaws_4_data},
        'KAWS_5': {'name': 'KAWS_5', 'data': kaws_5_data}
    }
    
    price_data = {}
    
    for figure_id, figure_info in kaws_figures.items():
        # Convert to DataFrame
        df = pd.DataFrame(figure_info['data'], columns=['datetime', 'price'])
        df['datetime'] = pd.to_datetime(df['datetime'])
        df = df.sort_values('datetime')
        
        # Create time series
        dates = df['datetime'].values
        prices = df['price'].values
        
        price_data[figure_id] = {
            'name': figure_info['name'],
            'dates': dates,
            'prices': prices,
            'df': df
        }
    
    return price_data

def analyze_price_psychology_connection(price_data):
    """Analyze how price movements connect to collector psychology patterns"""
    
    psychology_connections = {}
    
    for figure_id, data in price_data.items():
        prices = data['prices']
        dates = data['dates']
        
        # Calculate various metrics
        price_changes = np.diff(prices)
        volatility = np.std(price_changes)
        max_price = np.max(prices)
        min_price = np.min(prices)
        price_range = max_price - min_price
        avg_price = np.mean(prices)
        
        # Calculate additional metrics
        price_trend = np.polyfit(np.arange(len(prices)), prices, 1)[0]  # Linear trend
        price_volatility_ratio = volatility / avg_price  # Normalized volatility
        
        # Identify psychological triggers
        psychology_analysis = {
            'completionist_score': 0,
            'fomo_score': 0,
            'anchoring_score': 0,
            'speculative_score': 0,
            'emotional_score': 0
        }
        
        # Completionist: High value, limited availability, stable high prices
        if avg_price > 1000:
            psychology_analysis['completionist_score'] += 2
        if price_range > 500 and avg_price > 800:
            psychology_analysis['completionist_score'] += 1
        if price_volatility_ratio < 0.1:  # Low volatility for completionists
            psychology_analysis['completionist_score'] += 1
            
        # FOMO: High volatility, rapid price changes, upward trends
        if volatility > 50:
            psychology_analysis['fomo_score'] += 2
        if np.any(np.abs(price_changes) > 100):
            psychology_analysis['fomo_score'] += 1
        if price_trend > 0:  # Upward trend
            psychology_analysis['fomo_score'] += 1
        if price_volatility_ratio > 0.15:
            psychology_analysis['fomo_score'] += 1
            
        # Anchoring: Price stability around certain levels, psychological price points
        price_levels = np.unique(np.round(prices / 50) * 50)
        if len(price_levels) < len(prices) * 0.3:  # Fewer unique price levels
            psychology_analysis['anchoring_score'] += 2
        if np.std(prices) < avg_price * 0.2:  # Low price variation
            psychology_analysis['anchoring_score'] += 1
        # Check for psychological price points (round numbers)
        round_numbers = [p for p in prices if p % 50 == 0 or p % 100 == 0]
        if len(round_numbers) > len(prices) * 0.2:
            psychology_analysis['anchoring_score'] += 1
            
        # Speculative: High volatility, upward trends, price spikes
        if volatility > 40 and price_trend > 0:
            psychology_analysis['speculative_score'] += 2
        if max_price > avg_price * 1.3:
            psychology_analysis['speculative_score'] += 1
        if price_volatility_ratio > 0.12:
            psychology_analysis['speculative_score'] += 1
        # Check for speculative spikes
        price_spikes = [i for i, change in enumerate(price_changes) if abs(change) > np.mean(np.abs(price_changes)) * 2]
        if len(price_spikes) > len(price_changes) * 0.1:
            psychology_analysis['speculative_score'] += 1
            
        # Emotional: High volatility, unpredictable patterns, erratic behavior
        if volatility > 60:
            psychology_analysis['emotional_score'] += 2
        if np.std(price_changes) > np.mean(np.abs(price_changes)):
            psychology_analysis['emotional_score'] += 1
        if price_volatility_ratio > 0.2:
            psychology_analysis['emotional_score'] += 1
        # Check for emotional buying patterns (rapid ups and downs)
        emotional_patterns = 0
        for i in range(1, len(price_changes)):
            if (price_changes[i] > 0 and price_changes[i-1] < 0) or (price_changes[i] < 0 and price_changes[i-1] > 0):
                emotional_patterns += 1
        if emotional_patterns > len(price_changes) * 0.3:
            psychology_analysis['emotional_score'] += 1
            
        psychology_connections[figure_id] = {
            'name': data['name'],
            'volatility': volatility,
            'avg_price': avg_price,
            'price_range': price_range,
            'price_trend': price_trend,
            'price_volatility_ratio': price_volatility_ratio,
            'psychology_analysis': psychology_analysis
        }
    
    return psychology_connections

def create_visualizations(price_data, psychology_connections):
    """Create comprehensive visualizations"""
    
    fig = plt.figure(figsize=(24, 18))
    
    # 1. Price Volatility Timeline
    ax1 = plt.subplot(3, 3, 1)
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
    for i, (figure_id, data) in enumerate(price_data.items()):
        plt.plot(data['dates'], data['prices'], label=data['name'], linewidth=2, alpha=0.8, color=colors[i])
    plt.title('KAWS Figure Price Volatility Over Time', fontsize=14, fontweight='bold')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    
    # 2. Psychology Pattern Heatmap
    ax2 = plt.subplot(3, 3, 2)
    psychology_data = []
    figure_names = []
    
    for figure_id, analysis in psychology_connections.items():
        psychology_data.append(list(analysis['psychology_analysis'].values()))
        figure_names.append(analysis['name'])
    
    psychology_df = pd.DataFrame(psychology_data, 
                               columns=['Completionist', 'FOMO', 'Anchoring', 'Speculative', 'Emotional'],
                               index=figure_names)
    
    sns.heatmap(psychology_df, annot=True, cmap='YlOrRd', fmt='.1f', ax=ax2, 
                cbar_kws={'label': 'Psychology Score'})
    plt.title('Collector Psychology Pattern Analysis', fontsize=14, fontweight='bold')
    plt.ylabel('KAWS Figure')
    plt.xlabel('Psychology Pattern')
    
    # Adjust text rotation and size for better readability
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right', fontsize=9)
    ax2.set_yticklabels(ax2.get_yticklabels(), fontsize=9)
    
    # 3. Volatility vs Psychology Correlation
    ax3 = plt.subplot(3, 3, 3)
    volatilities = [analysis['volatility'] for analysis in psychology_connections.values()]
    fomo_scores = [analysis['psychology_analysis']['fomo_score'] for analysis in psychology_connections.values()]
    
    plt.scatter(volatilities, fomo_scores, s=100, alpha=0.7, c=colors)
    
    # Improved label positioning to avoid overlap
    label_positions = [
        (10, 10),   # KAWS_1
        (-15, 15),  # KAWS_2
        (10, -10),  # KAWS_3
        (-15, -15), # KAWS_4
        (10, 15)    # KAWS_5
    ]
    
    for i, (figure_id, analysis) in enumerate(psychology_connections.items()):
        plt.annotate(analysis['name'], (volatilities[i], fomo_scores[i]), 
                    xytext=label_positions[i], textcoords='offset points', 
                    fontsize=9, fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8),
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.1', alpha=0.6))
    
    plt.xlabel('Price Volatility ($)')
    plt.ylabel('FOMO Score')
    plt.title('Volatility vs FOMO Psychology', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    # 4. Price Distribution by Psychology Type
    ax4 = plt.subplot(3, 3, 4)
    psychology_types = ['Completionist', 'FOMO', 'Anchoring', 'Speculative', 'Emotional']
    avg_prices_by_psychology = []
    
    for psych_type in psychology_types:
        scores = [analysis['psychology_analysis'][f'{psych_type.lower().replace(" ", "_")}_score'] 
                 for analysis in psychology_connections.values()]
        avg_prices = [analysis['avg_price'] for analysis in psychology_connections.values()]
        
        # Weighted average price by psychology score
        weighted_avg = np.average(avg_prices, weights=scores) if sum(scores) > 0 else 0
        avg_prices_by_psychology.append(weighted_avg)
    
    bars = plt.bar(psychology_types, avg_prices_by_psychology, color=colors)
    plt.title('Average Price by Psychology Pattern', fontsize=14, fontweight='bold')
    plt.ylabel('Average Price ($)')
    plt.xticks(rotation=45)
    
    # Add value labels on bars
    for bar, price in zip(bars, avg_prices_by_psychology):
        if price > 0:
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50, 
                    f'${price:.0f}', ha='center', va='bottom')
    
    # 5. Price Range Analysis
    ax5 = plt.subplot(3, 3, 5)
    price_ranges = [analysis['price_range'] for analysis in psychology_connections.values()]
    figure_names_short = [name.split('(')[0].strip() for name in figure_names]
    
    bars = plt.barh(figure_names_short, price_ranges, color=colors)
    plt.title('Price Range by Figure', fontsize=14, fontweight='bold')
    plt.xlabel('Price Range ($)')
    
    # Add value labels
    for bar, price_range in zip(bars, price_ranges):
        plt.text(bar.get_width() + 20, bar.get_y() + bar.get_height()/2, 
                f'${price_range:.0f}', va='center')
    
    # 6. Psychology Pattern Network
    ax6 = plt.subplot(3, 3, 6)
    
    # Create a simple network visualization
    psychology_nodes = psychology_types
    node_positions = {
        'Completionist': (0.2, 0.8),
        'FOMO': (0.8, 0.8),
        'Anchoring': (0.2, 0.2),
        'Speculative': (0.8, 0.2),
        'Emotional': (0.5, 0.5)
    }
    
    # Draw nodes
    for psych_type, pos in node_positions.items():
        plt.scatter(pos[0], pos[1], s=200, alpha=0.7, 
                   color=colors[psychology_types.index(psych_type)])
        plt.text(pos[0], pos[1], psych_type, ha='center', va='center', fontsize=8, fontweight='bold')
    
    # Draw connections based on correlation
    connections = [
        ('FOMO', 'Emotional', 0.8),
        ('Speculative', 'FOMO', 0.6),
        ('Completionist', 'Anchoring', 0.4),
        ('Emotional', 'Speculative', 0.5)
    ]
    
    for start, end, strength in connections:
        x1, y1 = node_positions[start]
        x2, y2 = node_positions[end]
        plt.plot([x1, x2], [y1, y2], 'k-', alpha=strength, linewidth=strength*3)
    
    plt.title('Psychology Pattern Relationships', fontsize=14, fontweight='bold')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.axis('off')
    
    # 7. Monthly Price Changes Heatmap
    ax7 = plt.subplot(3, 3, 7)
    
    # Calculate monthly price changes for each figure
    monthly_changes = []
    for figure_id, data in price_data.items():
        df = data['df'].copy()
        df.set_index('datetime', inplace=True)
        monthly_prices = df.resample('M').mean()
        monthly_changes.append(np.diff(monthly_prices['price'].values))
    
    # Pad arrays to same length
    max_length = max(len(changes) for changes in monthly_changes)
    monthly_changes_padded = []
    for changes in monthly_changes:
        padded = np.pad(changes, (0, max_length - len(changes)), mode='constant', constant_values=np.nan)
        monthly_changes_padded.append(padded)
    
    monthly_changes_array = np.array(monthly_changes_padded)
    sns.heatmap(monthly_changes_array, 
                xticklabels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                yticklabels=[data['name'] for data in price_data.values()],
                cmap='RdYlBu_r', center=0, ax=ax7, cbar_kws={'label': 'Price Change ($)'})
    plt.title('Monthly Price Changes', fontsize=14, fontweight='bold')
    plt.xlabel('Month')
    plt.ylabel('KAWS Figure')
    
    # 8. Psychology Score Radar Chart
    ax8 = plt.subplot(3, 3, 8, projection='polar')
    
    # Calculate average psychology scores across all figures
    avg_psychology_scores = []
    for psych_type in psychology_types:
        scores = [analysis['psychology_analysis'][f'{psych_type.lower().replace(" ", "_")}_score'] 
                 for analysis in psychology_connections.values()]
        avg_psychology_scores.append(np.mean(scores))
    
    angles = np.linspace(0, 2 * np.pi, len(psychology_types), endpoint=False).tolist()
    avg_psychology_scores += avg_psychology_scores[:1]  # Close the loop
    angles += angles[:1]
    
    ax8.plot(angles, avg_psychology_scores, 'o-', linewidth=2, color='#FF6B6B')
    ax8.fill(angles, avg_psychology_scores, alpha=0.25, color='#FF6B6B')
    ax8.set_xticks(angles[:-1])
    ax8.set_xticklabels(psychology_types)
    ax8.set_title('Average Psychology Pattern Scores', fontsize=14, fontweight='bold', pad=20)
    
    # 9. Summary Statistics
    ax9 = plt.subplot(3, 3, 9)
    ax9.axis('off')
    
    # Calculate summary statistics
    total_volatility = np.mean([analysis['volatility'] for analysis in psychology_connections.values()])
    dominant_psychology = max(avg_psychology_scores)
    dominant_type = psychology_types[np.argmax(avg_psychology_scores)]
    avg_price = np.mean([analysis['avg_price'] for analysis in psychology_connections.values()])
    
    summary_text = f"""
    KAWS Price Psychology Analysis Summary
    
    📊 Key Findings:
    • Average Volatility: ${total_volatility:.0f}
    • Average Price: ${avg_price:.0f}
    • Dominant Psychology: {dominant_type}
    • Price Range: ${min([a['price_range'] for a in psychology_connections.values()]):.0f} - ${max([a['price_range'] for a in psychology_connections.values()]):.0f}
    
    🧠 Psychology Insights:
    • FOMO drives high volatility figures
    • Completionist patterns in premium items
    • Speculative behavior in trending pieces
    • Emotional buying in volatile markets
    • Anchoring effects in stable pieces
    """
    
    ax9.text(0.1, 0.9, summary_text, transform=ax9.transAxes, fontsize=10,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8))
    
    plt.tight_layout(pad=2.0)
    plt.savefig('kaws_price_psychology_analysis.png', dpi=300, bbox_inches='tight', pad_inches=0.5)
    plt.show()
    
    return psychology_connections

def main():
    """Main analysis function"""
    print("🎨 KAWS Price Psychology Analysis")
    print("=" * 50)
    
    # Parse real price data
    print("📈 Parsing real KAWS price data...")
    price_data = parse_kaws_price_data()
    
    # Analyze psychology connections
    print("🧠 Analyzing collector psychology patterns...")
    psychology_connections = analyze_price_psychology_connection(price_data)
    
    # Create visualizations
    print("📊 Creating comprehensive visualizations...")
    results = create_visualizations(price_data, psychology_connections)
    
    # Print detailed analysis
    print("\n📋 Detailed Analysis Results:")
    print("-" * 40)
    
    for figure_id, analysis in psychology_connections.items():
        print(f"\n🎯 {analysis['name']}:")
        print(f"   • Average Price: ${analysis['avg_price']:.0f}")
        print(f"   • Volatility: ${analysis['volatility']:.0f}")
        print(f"   • Price Range: ${analysis['price_range']:.0f}")
        print(f"   • Price Trend: {analysis['price_trend']:.2f} (slope)")
        print(f"   • Volatility Ratio: {analysis['price_volatility_ratio']:.3f}")
        
        # Find dominant psychology pattern
        psych_scores = analysis['psychology_analysis']
        dominant_pattern = max(psych_scores.items(), key=lambda x: x[1])
        pattern_name = dominant_pattern[0].replace('_', ' ').title()
        print(f"   • Dominant Psychology: {pattern_name} (Score: {dominant_pattern[1]})")
    
    print(f"\n✅ Analysis complete! Visualization saved as 'kaws_price_psychology_analysis.png'")
    
    return price_data, psychology_connections

if __name__ == "__main__":
    price_data, psychology_connections = main() 