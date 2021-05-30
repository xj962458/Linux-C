ui->textEdit->installEventFilter(this);
bool Widget::eventFilter(QObject *watched, QEvent *event)
{
    if (watched == ui->textEdit && event->type() == QEvent::KeyPress)
    {
        int key = (static_cast<QKeyEvent *>(event))->key();
        if (Qt::Key_Return == key || Qt::Key_Enter == key)
        {
            qDebug() << "Enter pressed";
            return true;
        }
    }
    return QWidget::eventFilter(watched, event);
}