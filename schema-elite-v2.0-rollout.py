#!/usr/bin/env python3
"""
schema-elite-v2.0-rollout.py

Applies elite JSON-LD schema (v2.0, 92/100 rating) to all 65 city landing pages.
Supports parametric city-specific configuration for @id, areaServed, and contact points.

Usage:
    python3 schema-elite-v2.0-rollout.py --dry-run
    python3 schema-elite-v2.0-rollout.py --apply
    python3 schema-elite-v2.0-rollout.py --city goiania-go --service aluguel-de-empilhadeira-combustao
"""

import json
import os
import re
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# City context database
CITIES = {
    'goiania-go': {
        'name': 'Goiânia',
        'state': 'GO',
        'lat': -16.7234,
        'lon': -49.2654,
        'phone': '+55-62-3211-1515',
        'whatsapp': '+55-62-99999999',
        'area_served_radius': 200000,
        'region': 'Goiás'
    },
    'brasilia-df': {
        'name': 'Brasília',
        'state': 'DF',
        'lat': -15.7867,
        'lon': -47.8784,
        'phone': '+55-61-3211-1515',
        'whatsapp': '+55-61-99999999',
        'area_served_radius': 200000,
        'region': 'Distrito Federal'
    },
    'anapolis-go': {
        'name': 'Anápolis',
        'state': 'GO',
        'lat': -16.3261,
        'lon': -48.9516,
        'phone': '+55-62-3211-1515',
        'whatsapp': '+55-62-99999999',
        'area_served_radius': 180000,
        'region': 'Goiás'
    },
    'aparecida-de-goiania-go': {
        'name': 'Aparecida de Goiânia',
        'state': 'GO',
        'lat': -16.8255,
        'lon': -49.0294,
        'phone': '+55-62-3211-1515',
        'whatsapp': '+55-62-99999999',
        'area_served_radius': 180000,
        'region': 'Goiás'
    },
    'uruacu-go': {
        'name': 'Uruaçu',
        'state': 'GO',
        'lat': -15.4523,
        'lon': -49.1161,
        'phone': '+55-62-3211-1515',
        'whatsapp': '+55-62-99999999',
        'area_served_radius': 160000,
        'region': 'Goiás'
    },
    'senador-canedo-go': {
        'name': 'Senador Canedo',
        'state': 'GO',
        'lat': -16.708,
        'lon': -49.092,
        'phone': '+55-62-3211-1515',
        'whatsapp': '+55-62-99999999',
        'area_served_radius': 180000,
        'region': 'Goiás'
    },
    'trindade-go': {
        'name': 'Trindade',
        'state': 'GO',
        'lat': -16.8667,
        'lon': -49.4667,
        'phone': '+55-62-3211-1515',
        'whatsapp': '+55-62-99999999',
        'area_served_radius': 160000,
        'region': 'Goiás'
    },
    'inhumas-go': {
        'name': 'Inhumas',
        'state': 'GO',
        'lat': -16.3511,
        'lon': -49.1544,
        'phone': '+55-62-3211-1515',
        'whatsapp': '+55-62-99999999',
        'area_served_radius': 160000,
        'region': 'Goiás'
    },
    'caldas-novas-go': {
        'name': 'Caldas Novas',
        'state': 'GO',
        'lat': -17.7481,
        'lon': -48.6095,
        'phone': '+55-64-3211-1515',
        'whatsapp': '+55-64-99999999',
        'area_served_radius': 140000,
        'region': 'Goiás'
    },
    'itumbiara-go': {
        'name': 'Itumbiara',
        'state': 'GO',
        'lat': -18.4161,
        'lon': -49.2167,
        'phone': '+55-64-3211-1515',
        'whatsapp': '+55-64-99999999',
        'area_served_radius': 140000,
        'region': 'Goiás'
    },
    'catalao-go': {
        'name': 'Catalão',
        'state': 'GO',
        'lat': -18.1544,
        'lon': -47.9361,
        'phone': '+55-64-3211-1515',
        'whatsapp': '+55-64-99999999',
        'area_served_radius': 140000,
        'region': 'Goiás'
    },
    'jatai-go': {
        'name': 'Jataí',
        'state': 'GO',
        'lat': -17.8847,
        'lon': -51.7181,
        'phone': '+55-64-3211-1515',
        'whatsapp': '+55-64-99999999',
        'area_served_radius': 140000,
        'region': 'Goiás'
    },
    'luziania-go': {
        'name': 'Luziânia',
        'state': 'GO',
        'lat': -15.8267,
        'lon': -48.1633,
        'phone': '+55-61-3211-1515',
        'whatsapp': '+55-61-99999999',
        'area_served_radius': 160000,
        'region': 'Goiás'
    },
}

SERVICE_MAPPING = {
    'aluguel-de-empilhadeira-combustao': 'service-empilhadeira-combustao',
    'aluguel-de-empilhadeira-eletrica': 'service-empilhadeira-eletrica',
    'aluguel-de-transpaleteira': 'service-transpaleteira',
    'aluguel-de-plataforma-elevatoria-articulada': 'service-plataforma-articulada',
    'aluguel-de-plataforma-elevatoria-tesoura': 'service-plataforma-tesoura',
}

def load_base_schema() -> Dict:
    """Load the base elite schema from v2.0 file."""
    schema_path = Path('/Users/jrios/move-maquinas-seo/schema-elite-v2.0-PRONTO-DEPLOY.json')
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def parametrize_schema(base_schema: Dict, city_key: str, service_key: str) -> Dict:
    """Parametrize schema for specific city and service."""
    schema = json.loads(json.dumps(base_schema))  # Deep copy

    city = CITIES.get(city_key)
    if not city:
        logger.warning(f"City {city_key} not found in database")
        return schema

    service_name = SERVICE_MAPPING.get(service_key, service_key)
    city_url = f"https://movemaquinas.com.br/{city_key}/"
    service_url = f"{city_url}{service_key}/"

    # Update Organization node
    for node in schema.get('@graph', []):
        if node.get('@id') == 'https://movemaquinas.com.br/#organization':
            node['geo']['latitude'] = city['lat']
            node['geo']['longitude'] = city['lon']
            node['serviceArea']['geoMidpoint']['latitude'] = city['lat']
            node['serviceArea']['geoMidpoint']['longitude'] = city['lon']
            # Update phone/whatsapp with city-specific values if available
            if city.get('whatsapp'):
                for cp in node.get('contactPoint', []):
                    if cp.get('contactType') == 'Customer Service':
                        cp['telephone'] = city['whatsapp']
                        cp['url'] = f"https://wa.me/{city['whatsapp'].replace('+', '').replace('-', '')}?text=Oi%20preciso%20alugar%20{service_key.replace('-', '%20')}"

        # Update WebPage node
        elif node.get('@id') == 'https://movemaquinas.com.br/goiania-go/aluguel-de-empilhadeira-combustao/#webpage':
            node['@id'] = f"{service_url}#webpage"
            node['url'] = service_url

        # Update Service node
        elif node.get('@id') == 'https://movemaquinas.com.br/#service-empilhadeira-combustao':
            node['@id'] = f"https://movemaquinas.com.br/#{service_name}"
            node['areaServed']['name'] = city['name']
            node['areaServed']['addressRegion'] = city['state']

        # Update HowTo node
        elif node.get('@type') == 'HowTo' and node.get('@id'):
            node['@id'] = f"https://movemaquinas.com.br/#howto-{service_key.replace('aluguel-de-', '').replace('-', '-')}"

        # Update FAQPage node
        elif node.get('@type') == 'FAQPage':
            node['@id'] = f"https://movemaquinas.com.br/#{city_key}-faqpage"

        # Update BreadcrumbList
        elif node.get('@type') == 'BreadcrumbList':
            if node.get('itemListElement'):
                node['itemListElement'][1]['name'] = f"Equipamentos em {city['name']}"
                node['itemListElement'][1]['item'] = city_url
                node['itemListElement'][2]['name'] = f"{node['itemListElement'][2]['name'].split(' em ')[0]} em {city['name']}"
                node['itemListElement'][2]['item'] = service_url

    return schema

def remove_existing_schema(html_content: str) -> str:
    """Remove existing JSON-LD script tag from HTML."""
    pattern = r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>.*?</script>'
    return re.sub(pattern, '', html_content, flags=re.DOTALL)

def inject_schema(html_content: str, schema: Dict, position: str = 'head') -> str:
    """Inject JSON-LD schema into HTML."""
    # Remove existing schema first
    html_content = remove_existing_schema(html_content)

    schema_str = json.dumps(schema, ensure_ascii=False, separators=(',', ':'))
    script_tag = f'\n<script type="application/ld+json">{schema_str}</script>\n'

    if position == 'head':
        # Insert before closing </head>
        html_content = html_content.replace('</head>', f'{script_tag}</head>', 1)
    else:
        # Insert before closing </body>
        html_content = html_content.replace('</body>', f'{script_tag}</body>', 1)

    return html_content

def process_landing_page(city_key: str, service_key: str, dry_run: bool = True) -> bool:
    """Process a single landing page."""
    lp_path = Path(f'/Users/jrios/move-maquinas-seo/{city_key}/{service_key}/index.html')

    if not lp_path.exists():
        logger.warning(f"Landing page not found: {lp_path}")
        return False

    try:
        # Read HTML
        with open(lp_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Load and parametrize schema
        base_schema = load_base_schema()
        schema = parametrize_schema(base_schema, city_key, service_key)

        # Inject schema
        updated_html = inject_schema(html_content, schema)

        if not dry_run:
            # Write back to file
            with open(lp_path, 'w', encoding='utf-8') as f:
                f.write(updated_html)
            logger.info(f"✓ Updated: {city_key}/{service_key}")
        else:
            logger.info(f"[DRY] Would update: {city_key}/{service_key}")

        return True

    except Exception as e:
        logger.error(f"Error processing {city_key}/{service_key}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Apply elite schema v2.0 to city LPs')
    parser.add_argument('--dry-run', action='store_true', default=True,
                        help='Preview changes without writing (default: True)')
    parser.add_argument('--apply', action='store_true',
                        help='Apply changes to files')
    parser.add_argument('--city', type=str,
                        help='Process only specific city (e.g., goiania-go)')
    parser.add_argument('--service', type=str,
                        help='Process only specific service (e.g., aluguel-de-empilhadeira-combustao)')

    args = parser.parse_args()

    dry_run = not args.apply

    if args.city and args.service:
        # Single LP
        process_landing_page(args.city, args.service, dry_run=dry_run)
    else:
        # All LPs
        cities_to_process = [args.city] if args.city else list(CITIES.keys())
        services_to_process = [args.service] if args.service else list(SERVICE_MAPPING.keys())

        total = len(cities_to_process) * len(services_to_process)
        processed = 0

        logger.info(f"Processing {total} landing pages (dry_run={dry_run})")

        for city in cities_to_process:
            for service in services_to_process:
                if process_landing_page(city, service, dry_run=dry_run):
                    processed += 1

        logger.info(f"Processed: {processed}/{total}")

if __name__ == '__main__':
    main()
