import pandas as pd
import sqlite3

# -----------------------------------
# PLANETS DATABASE
# -----------------------------------

conn1 = sqlite3.connect('planets.db')

# 1
df_no_moons = pd.read_sql("""
SELECT *
FROM planets
WHERE num_of_moons = 0;
""", conn1)

# 2
df_name_seven = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE LENGTH(name) = 7;
""", conn1)

# 3
df_mass = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE mass <= 1.00;
""", conn1)

# 4
df_mass_moon = pd.read_sql("""
SELECT *
FROM planets
WHERE num_of_moons >= 1
AND mass < 1.00;
""", conn1)

# 5
df_blue = pd.read_sql("""
SELECT name, color
FROM planets
WHERE color LIKE '%blue%';
""", conn1)

# -----------------------------------
# DOGS DATABASE
# -----------------------------------

conn2 = sqlite3.connect('dogs.db')

# 6
df_hungry = pd.read_sql("""
SELECT name, age, breed
FROM dogs
WHERE hungry = 1
ORDER BY age ASC;
""", conn2)

df_hungry = df_hungry.astype(object).where(pd.notnull(df_hungry), None)

# extra test variable
df_hungry_ages = pd.read_sql("""
SELECT name, age
FROM dogs
WHERE hungry = 1
AND age IN (4, 7, 6, 3)
ORDER BY 
    CASE age
        WHEN 4 THEN 1
        WHEN 7 THEN 2
        WHEN 6 THEN 3
        WHEN 3 THEN 4
END;
""", conn2)

# 7
df_age = pd.read_sql("""
SELECT name, age, hungry
FROM dogs
WHERE hungry = 1
AND age BETWEEN 2 AND 7
ORDER BY name ASC;
""", conn2)

# 8
df_4_oldest = pd.read_sql("""
SELECT name, age, breed
FROM dogs
WHERE name IN ('Pickles', 'McGruff', 'Snowy', 'Lassie')
ORDER BY 
    CASE name
        WHEN 'Pickles' THEN 1
        WHEN 'McGruff' THEN 2
        WHEN 'Snowy' THEN 3
        WHEN 'Lassie' THEN 4
END;
""", conn2)

# -----------------------------------
# BABE RUTH DATABASE
# -----------------------------------

conn3 = sqlite3.connect('babe_ruth.db')

# 9
df_ruth_years = pd.read_sql("""
SELECT COUNT(*) AS years_played
FROM babe_ruth_stats;
""", conn3)

# 10
df_hr_total = pd.read_sql("""
SELECT SUM(HR) AS total_home_runs
FROM babe_ruth_stats;
""", conn3)

# 11
df_teams_years = pd.read_sql("""
SELECT team, COUNT(*) AS number_years
FROM babe_ruth_stats
GROUP BY team;
""", conn3)

# 12
df_at_bats = pd.read_sql("""
SELECT team, AVG(at_bats) AS average_at_bats
FROM babe_ruth_stats
GROUP BY team
HAVING AVG(at_bats) > 200;
""", conn3)

# 13
conn1.close()
conn2.close()
conn3.close()

