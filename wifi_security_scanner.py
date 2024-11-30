#!/usr/bin/env python3

# Owner: 0nehack
# Please do not modify the code
#This code is for testing purposes
#I’m not responsible for illegally use my code
# Date: 11-30-2024

import asyncio
from datetime import datetime
import random
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress
from rich.layout import Layout
from rich.live import Live
from rich.text import Text
from rich.tree import Tree
from rich.columns import Columns

# Simulated test data
TEST_NETWORKS = [
    {
        'ssid': 'HomeNetwork_2.4G',
        'bssid': '00:11:22:33:44:55',
        'encryption': 'WPA2',
        'signal_strength': -65,
        'channel': 6,
        'pmf_enabled': True,
        'client_isolation': True,
        'rate_limiting': True
    },
    {
        'ssid': 'CoffeeShop_FREE',
        'bssid': 'AA:BB:CC:DD:EE:FF',
        'encryption': 'WPA',
        'signal_strength': -72,
        'channel': 1,
        'pmf_enabled': False,
        'client_isolation': False,
        'rate_limiting': False
    },
    {
        'ssid': 'Company_Network',
        'bssid': '11:22:33:44:55:66',
        'encryption': 'WPA2-Enterprise',
        'signal_strength': -58,
        'channel': 11,
        'pmf_enabled': True,
        'client_isolation': True,
        'rate_limiting': True,
        'mac_filtering': True
    },
    {
        'ssid': 'OpenNetwork',
        'bssid': 'FF:EE:DD:CC:BB:AA',
        'encryption': 'None',
        'signal_strength': -67,
        'channel': 3,
        'pmf_enabled': False,
        'client_isolation': False,
        'rate_limiting': False
    },
    {
        'ssid': 'WeakSignal_Network',
        'bssid': '99:88:77:66:55:44',
        'encryption': 'WPA2',
        'signal_strength': -89,
        'channel': 9,
        'pmf_enabled': True,
        'client_isolation': True
    },
    {
        'ssid': 'Guest_Network_Public',
        'bssid': '33:44:55:66:77:88',
        'encryption': 'WPA2',
        'signal_strength': -70,
        'channel': 1,
        'pmf_enabled': False,
        'client_isolation': False,
        'vlan_isolated': False
    },
    {
        'ssid': 'Old_WEP_Network',
        'bssid': '22:33:44:55:66:77',
        'encryption': 'WEP',
        'signal_strength': -75,
        'channel': 6,
        'hidden_ssid': True
    },
    {
        'ssid': 'Modern_WPA3_Network',
        'bssid': 'BB:CC:DD:EE:FF:00',
        'encryption': 'WPA3',
        'signal_strength': -62,
        'channel': 36,
        'pmf_enabled': True,
        'client_isolation': True,
        'rate_limiting': True,
        'mac_filtering': True,
        'dhcp_snooping': True
    }
]

# Enhanced attack signatures
TEST_ATTACKS = [
    {
        'type': 'Evil Twin Attack',
        'severity': 'High',
        'confidence': 85,
        'indicators': 'Duplicate SSID with different BSSID detected',
        'mitigation': 'Enable MAC address filtering and client isolation'
    },
    {
        'type': 'Deauthentication Attack',
        'severity': 'Critical',
        'confidence': 95,
        'indicators': 'Mass deauth packets detected from unauthorized source',
        'mitigation': 'Implement 802.11w Protected Management Frames'
    },
    {
        'type': 'KRACK Attack',
        'severity': 'Critical',
        'confidence': 90,
        'indicators': 'WPA2 4-way handshake manipulation detected',
        'mitigation': 'Update all devices to support WPA3 or patched WPA2'
    },
    {
        'type': 'Pixie Dust Attack',
        'severity': 'High',
        'confidence': 80,
        'indicators': 'Multiple WPS authentication attempts with timing patterns',
        'mitigation': 'Disable WPS or upgrade to WPS 2.0'
    },
    {
        'type': 'Beacon Flood',
        'severity': 'Medium',
        'confidence': 75,
        'indicators': 'Unusual volume of beacon frames from multiple SSIDs',
        'mitigation': 'Configure WIDS/WIPS to detect and block beacon floods'
    },
    {
        'type': 'Man-in-the-Middle',
        'severity': 'Critical',
        'confidence': 88,
        'indicators': 'ARP spoofing detected, suspicious gateway redirections',
        'mitigation': 'Implement 802.1X authentication and monitor ARP tables'
    },
    {
        'type': 'PMKID Attack',
        'severity': 'High',
        'confidence': 82,
        'indicators': 'Repeated EAPOL handshake requests without authentication',
        'mitigation': 'Use strong WPA2/WPA3 passwords and enable PMF'
    }
]

async def simulate_scan():
    """Simulate a network scan with progress updates"""
    with Progress() as progress:
        scan_task = progress.add_task("[cyan]Scanning networks...", total=100)
        crypto_task = progress.add_task("[green]Analyzing security...", total=100)
        attack_task = progress.add_task("[red]Detecting attacks...", total=100)
        
        # Simulate scanning progress
        while not progress.finished:
            await asyncio.sleep(0.1)
            progress.update(scan_task, advance=1)
            progress.update(crypto_task, advance=0.7)
            progress.update(attack_task, advance=0.5)

def analyze_vulnerabilities(network):
    """Analyze network vulnerabilities with enhanced checks"""
    vulns = []
    
    # Encryption Protocol Vulnerabilities
    if network['encryption'] == 'WPA':
        vulns.append("Outdated encryption protocol (WPA)")
        vulns.append("Vulnerable to TKIP attacks")
        vulns.append("No Perfect Forward Secrecy")
    elif network['encryption'] == 'WEP':
        vulns.append("Severely outdated encryption (WEP)")
        vulns.append("Vulnerable to FMS attack")
        vulns.append("Vulnerable to chopchop attack")
        vulns.append("Weak IV implementation")
    elif network['encryption'] == 'None':
        vulns.append("No encryption - all traffic can be intercepted")
        vulns.append("Vulnerable to passive eavesdropping")
    elif network['encryption'] == 'WPA2':
        if random.random() < 0.3:  # Simulate detection of older WPA2 implementation
            vulns.append("Potentially vulnerable to KRACK attack")
        if network.get('wps_enabled', False):
            vulns.append("WPS could be vulnerable to brute force")
    
    # Signal Strength Analysis
    if network['signal_strength'] > -70:
        vulns.append("Strong signal strength may allow long-range attacks")
    elif network['signal_strength'] < -80:
        vulns.append("Weak signal may cause frequent disconnections")
    
    # Channel Analysis
    if network['channel'] in [1, 6, 11]:
        overlapping = random.randint(1, 3)  # Simulate detection of overlapping networks
        if overlapping > 2:
            vulns.append(f"High channel congestion on channel {network['channel']}")
    
    # Management Frame Protection
    if not network.get('pmf_enabled', False):
        vulns.append("Management frames not protected (PMF disabled)")
        vulns.append("Vulnerable to deauthentication attacks")
    
    # Client Isolation Check
    if not network.get('client_isolation', False):
        vulns.append("Client isolation not enabled")
        vulns.append("Lateral movement between clients possible")
    
    # DHCP Security
    if network.get('dhcp_snooping', False) == False:
        vulns.append("DHCP snooping not enabled")
        vulns.append("Vulnerable to rogue DHCP servers")
    
    # Rate Limiting
    if not network.get('rate_limiting', False):
        vulns.append("No rate limiting configured")
        vulns.append("Vulnerable to resource exhaustion attacks")
    
    # MAC Filtering
    if not network.get('mac_filtering', False):
        vulns.append("MAC address filtering not enabled")
    
    # Hidden SSID Check
    if network.get('hidden_ssid', False):
        vulns.append("Hidden SSID provides false sense of security")
    
    # Guest Network Segregation
    if 'GUEST' in network['ssid'].upper() and not network.get('vlan_isolated', False):
        vulns.append("Guest network not properly segregated")
        vulns.append("Potential access to internal networks")
    
    return vulns

def generate_recommendations(vulnerabilities):
    """Enhanced recommendation generation with prioritization and categorization"""
    recommendations = {
        'critical': [],
        'high': [],
        'medium': [],
        'low': []
    }
    
    # Critical Priority Recommendations
    if any(v.lower().startswith(("no encryption", "severely outdated")) for v in vulnerabilities):
        recommendations['critical'].append({
            'title': "Immediate Encryption Upgrade Required",
            'steps': [
                "Upgrade to WPA3 or latest WPA2 implementation",
                "Enable Protected Management Frames (PMF)",
                "Use strong, unique passwords (minimum 12 characters)",
                "Consider implementing 802.1X authentication"
            ]
        })

    if any("vulnerable to krack" in v.lower() for v in vulnerabilities):
        recommendations['critical'].append({
            'title': "KRACK Vulnerability Mitigation",
            'steps': [
                "Update all access points to latest firmware",
                "Enable Protected Management Frames",
                "Update all client devices",
                "Consider upgrade to WPA3"
            ]
        })

    # High Priority Recommendations
    if any("management frames not protected" in v.lower() for v in vulnerabilities):
        recommendations['high'].append({
            'title': "Management Frame Protection",
            'steps': [
                "Enable 802.11w Protected Management Frames",
                "Configure PMF as required for new clients",
                "Update legacy devices or segregate them"
            ]
        })

    if any("client isolation not enabled" in v.lower() for v in vulnerabilities):
        recommendations['high'].append({
            'title': "Network Isolation Implementation",
            'steps': [
                "Enable client isolation on all APs",
                "Implement VLAN segregation",
                "Configure proper firewall rules",
                "Enable MAC address filtering"
            ]
        })

    # Medium Priority Recommendations
    if any("channel congestion" in v.lower() for v in vulnerabilities):
        recommendations['medium'].append({
            'title': "Channel Optimization",
            'steps': [
                "Perform site survey to identify optimal channels",
                "Configure automatic channel selection",
                "Consider dual-band operation",
                "Adjust AP power levels"
            ]
        })

    if any("dhcp snooping not enabled" in v.lower() for v in vulnerabilities):
        recommendations['medium'].append({
            'title': "DHCP Security Enhancement",
            'steps': [
                "Enable DHCP snooping",
                "Configure trusted DHCP server ports",
                "Implement ARP inspection",
                "Set up DHCP rate limiting"
            ]
        })

    # Low Priority Recommendations
    if any("signal strength" in v.lower() for v in vulnerabilities):
        recommendations['low'].append({
            'title': "Signal Optimization",
            'steps': [
                "Optimize AP placement",
                "Adjust transmission power",
                "Consider additional APs for coverage",
                "Perform regular site surveys"
            ]
        })

    return recommendations

def calculate_risk_score(network):
    """Calculate network risk score"""
    base_score = {
        'WPA3': 1,
        'WPA2-Enterprise': 2,
        'WPA2': 3,
        'WPA': 7,
        'WEP': 9,
        'None': 10
    }.get(network['encryption'], 5)
    
    # Adjust for signal strength
    signal_modifier = abs(network['signal_strength']) / 100
    return min(10, base_score + signal_modifier)

def display_results():
    """Enhanced display format with better visualization"""
    console = Console()
    
    # Header with scan information
    console.print("\n[bold cyan]═══ WiFi Security Analysis Report ═══", justify="center")
    console.print(f"Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    console.print(f"Networks Analyzed: {len(TEST_NETWORKS)}")
    console.print(f"Attacks Detected: {len(TEST_ATTACKS)}\n")
    
    # Network Overview Section
    network_table = Table(
        title="[bold]Network Overview",
        expand=True,
        border_style="cyan"
    )
    network_table.add_column("SSID", style="cyan", no_wrap=True)
    network_table.add_column("Security", style="green")
    network_table.add_column("Signal", justify="right")
    network_table.add_column("Risk Score", justify="center")
    network_table.add_column("Status", justify="right")
    
    for network in TEST_NETWORKS:
        risk_score = calculate_risk_score(network)
        status = "✓ Secure" if risk_score < 3 else "⚠ Warning" if risk_score < 7 else "✗ Critical"
        color = "green" if risk_score < 3 else "yellow" if risk_score < 7 else "red"
        
        network_table.add_row(
            network['ssid'],
            network['encryption'],
            f"{network['signal_strength']} dBm",
            f"[{color}]{risk_score}/10",
            f"[{color}]{status}"
        )
    
    console.print(network_table)
    
    # Vulnerability Analysis Section
    console.print("\n[bold yellow]═══ Vulnerability Analysis ═══")
    for network in TEST_NETWORKS:
        vulns = analyze_vulnerabilities(network)
        if vulns:
            vuln_tree = Tree(
                f"[bold cyan]{network['ssid']} [white]({network['encryption']})"
            )
            
            # Group vulnerabilities by severity
            critical_vulns = [v for v in vulns if "severely" in v.lower() or "no encryption" in v.lower()]
            high_vulns = [v for v in vulns if "vulnerable to" in v.lower()]
            other_vulns = [v for v in vulns if v not in critical_vulns and v not in high_vulns]
            
            if critical_vulns:
                crit_branch = vuln_tree.add("[red]Critical Vulnerabilities")
                for v in critical_vulns:
                    crit_branch.add(f"[red]• {v}")
            
            if high_vulns:
                high_branch = vuln_tree.add("[yellow]High-Risk Vulnerabilities")
                for v in high_vulns:
                    high_branch.add(f"[yellow]• {v}")
            
            if other_vulns:
                other_branch = vuln_tree.add("[blue]Other Findings")
                for v in other_vulns:
                    other_branch.add(f"[blue]• {v}")
            
            console.print(vuln_tree)
    
    # Attack Detection Section
    console.print("\n[bold red]═══ Active Threats Detected ═══")
    attack_table = Table(show_header=True, border_style="red")
    attack_table.add_column("Attack Type", style="red")
    attack_table.add_column("Severity", style="yellow")
    attack_table.add_column("Confidence", justify="right")
    attack_table.add_column("Mitigation", style="green")
    
    for attack in TEST_ATTACKS:
        attack_table.add_row(
            attack['type'],
            attack['severity'],
            f"{attack['confidence']}%",
            attack.get('mitigation', 'N/A')
        )
    
    console.print(attack_table)
    
    # Recommendations Section
    console.print("\n[bold green]═══ Security Recommendations ═══")
    recommendations = generate_recommendations(vulns)
    
    for priority, rec_list in recommendations.items():
        if rec_list:
            color = {
                'critical': 'red',
                'high': 'yellow',
                'medium': 'blue',
                'low': 'green'
            }[priority]
            
            priority_panel = Panel(
                "\n".join([
                    f"[bold]{rec['title']}[/bold]\n" +
                    "\n".join(f"• {step}" for step in rec['steps'])
                    for rec in rec_list
                ]),
                title=f"[{color}]{priority.upper()} Priority",
                border_style=color
            )
            console.print(priority_panel)

async def main():
    console =

async def main():
    """Main execution function"""
    console = Console()
    
    # Display startup banner
    console.print("\n[bold cyan]╔════════════════════════════════════════╗")
    console.print("[bold cyan]║    WiFi Security Scanner Starting...    ║")
    console.print("[bold cyan]╚════════════════════════════════════════╝\n")
    
    try:
        # Start the scanning simulation
        console.print("[yellow]Initializing scan sequence...")
        await simulate_scan()
        
        # Display the results
        console.print("[green]Scan completed successfully! Generating report...\n")
        display_results()
        
        # Final status
        console.print("\n[bold cyan]═══ Scan Summary ═══")
        console.print("[green]✓ Network scanning completed")
        console.print("[green]✓ Vulnerability analysis completed")
        console.print("[green]✓ Attack detection completed")
        console.print("[green]✓ Recommendations generated")
        
        # Disclaimer
        console.print("\n[yellow]Disclaimer:", style="bold")
        console.print("This scan provides a point-in-time assessment of visible wireless networks.")
        console.print("Regular security audits are recommended for continuous protection.")
        
    except Exception as e:
        console.print(f"\n[bold red]Error during scan: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        Console().print("\n[bold red]Scan interrupted by user. Exiting...")
        exit(1)
    except Exception as e:
        Console().print(f"\n[bold red]Unexpected error: {str(e)}")
        exit(1) 
