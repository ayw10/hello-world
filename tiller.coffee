data = database.impala.query("""SELECT openconversations AS 'Open Conversations'
          FROM alice.respondly
          ORDER BY time desc
          LIMIT 1""")

table(data)

rangeGroups = Resultset.build 'group label', ->
  @push 'day'
  @push 'week'
  @push 'month'

param 'rangeGroup', select(rangeGroups), label: 'See last', initial: 'day'

onParam 'rangeGroup', ->
  switch params.rangeGroup
    when 'day'
      linechart(database.impala.query("""SELECT time, openconversations AS 'Open Conversations'
        FROM alice.respondly
        WHERE time > now() - interval 1 day
        ORDER BY time asc"""))
     when 'week'
      linechart(database.impala.query("""SELECT time, openconversations AS 'Open Conversations'
        FROM alice.respondly
        WHERE time > now() - interval 1 week
        ORDER BY time asc"""))
     when 'month'
      linechart(database.impala.query("""SELECT time, openconversations AS 'Open Conversations'
        FROM alice.respondly
        WHERE time > now() - interval 1 month
        ORDER BY time asc"""))