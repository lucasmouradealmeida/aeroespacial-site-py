const getDateNowForChat = () => {
  const options = {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false
  }

  const now = new Date()
  const formattedDate = new Intl.DateTimeFormat('pt-BR', options).format(now)

  return formattedDate.replace(',', '').replace(':', 'h')
}

export { getDateNowForChat }
